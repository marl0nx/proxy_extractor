from proxy_extractor import extract_proxies


def main():
    print('Extracting proxies from websites ...')
    with open('extracted.txt', 'w') as file:
        for _ in extract_proxies(['https://openproxy.space/list/http', 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt']):
            file.write(_ + '\n')
            print(_)


if __name__ == '__main__':
    main()

import sys
import time

import dns.resolver


def main():
    if len(sys.argv) < 3:
        return
    nameserver = sys.argv[-1]
    hostname = sys.argv[-2]
    # print(nameserver)
    # print(hostname)
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [nameserver]
    start = time.time()
    try:
        result = resolver.query(hostname)
    except:
        print('Domain {} was not found by the server'.format(hostname))
    else:
        end = time.time()
        difference = end - start
        answer = str(result.rrset).split(' ')[-1]
        print('DNS OK: {} second response time. {} returns {}|time={}s;;;0.000000'.format(
            round(difference, 3),
            hostname,
            answer,
            round(difference, 6)
        ))

if __name__ == '__main__':
    main()

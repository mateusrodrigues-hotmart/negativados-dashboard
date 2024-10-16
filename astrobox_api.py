import json
import requests


# put your authorization token here
TOKEN = 'H4sIAAAAAAAAAG1U2ZajOAz9ou5jSEiKxxCWgopNMLZZXvoEU4TFJKnJQuDrR6SnZ3rmzIPBlmTpSrrW5xjUhSebsAliPvkaafyrf6KG3Porv7ukYhuY3z%2FHQJO6GFPdqIuEz8a3LKWqTPFd9mYne3UqEzFFXv0oPa2Wp%2Bie6eYtnFSX225PJtHtkghhlt2Il2nhFhmhLeodyxXx3D5kzoJMeYtfwUlbLCzlt5fCPwUqS6Jmtw0WEAPlcVDC%2FlwsoluZEiUbANk6Ora7EbdHI0RaXXpCk6NlFe%2F0UvZvR6Y%2F4S8usneO%2FDes4eQsSbMciX28YybHXcuNcOJo1x6nXYth8SHUf%2FkzxkKn4yEptTwlm4NnoiJxx3JrtIWO1rBHeSqm32vxt419fRImdcJ8yJ8jbG%2BGEAVjlpJL8b86FVJHJTGnIuLPinKDx4LmIXLRIc0fIRJhqAlG57s9XoQsb0mMFlnvjDsWLXGPbxngJyNa4HYzYZ02Wc913DtriLEgLYecHY3YEdRtc3%2FVzd5omB1nDCP0YsTsOkB94H43hHa0JG034Sla58JVBdd2NC1xNik3SYwwm4KvgzMMQgsarhsU68KDPg8h88fQ7iBmtgT%2FOp6yOd6AAXduly3xgh6PaMgT0gHuMe%2F9W2jLRTbnMs162mBWQibdOu%2Fdq9T5OpwgZ%2FAD%2F%2FWv5TdDk6f14Ldn0PkGbuccMwN4UpcpBa4El9JTSo7%2BKhkDxh03jtHTTecaCn%2Fm1j8y5GLu1NZvuih2FYs5sZhrRrwzHcEJTzXix8Iic29SzbK4ouFf9nqeGF2e0IecuawsPxEkiMAv2MUMQU%2B1F599ptHZX0VV4FKuBYKjWR4wRV2qBZZw1J4pk1Pu2rHjbpkjKsYFiToRc1QHfDv7L92oU2H0M%2Fbsk0Qi4Cl6BqITFdjyKAa7zo1iYdqgcwC74K615%2BqFI2KOy2lnxkyYkGcZCrGZ5eMhnd8hnveaXIgaeP1IF0STnjmWHp%2FlwP1nnfXmmP3K9%2FQv%2FUN6AnhOL4VuTHOf5HvwyN8FKhYvvK3UzKlMrYc8UTXr55kBNnUOPuYzn2vb3TAVZiREMNcB%2BmJ6UBMOZ%2Fc%2FNjx2BPmv%2FjUnlNnI5jU7vkqvg%2FnlA1eOY%2BhhA2%2B1Npu6CTgI3DzeQIbIFj0x86fQ88dM58D9n3gL4FFxotUBZhLMQEX6AHoNbGvgrU18CT6MkEl4f6TFWzThhNRYdwbMRIthblbRd7t%2F3hrj4cZvFb5sLl%2F2p%2FRrdVx%2FO98DqyebEyLWsed7Qw7Vt2htit2kpSfnx5Y1G%2F2sm5Y9LcghzS7V8jpYee4FjN20LPlSRdpNjySwhoU5HNgktg0tu6%2FaW8WVKe%2FHz8N7ZXZHvXCTc5R757fa9%2BDLk%2FTwLit%2BgnQ8Vtpe92YK67mryMoiP6gX51qOG%2F0jW%2F6xW6oh2dtFc76bfYq7zDu3zf2x0tsYGdfLm7c317vN6cfyK%2FH3qGqpTPFgdePV0mverc%2Fqnr5bafMI%2FMPWXTUfzxVft0c0nk1%2B0wyMGLvW7vLQDyrIytvy5D66N92Izf7jQLrV9sT2tut9a%2FKnVtYh3t3eyOdHedzLXIv%2BBN8aavzGBgAA'


def run_query():
    '''
    Executes an example query on Astrobox and streams the results
    '''

    print('Requesting query execution')
    response = requests.post(
        'https://api-astrobox.buildstaging.com/v1/executor/reactive/by-alias',
        headers={
            'Authorization': f"Bearer {TOKEN}"
        },
        json={
            'query': 'query_streaming_ex',
            'saveResult': False,
            'parameters': {
                'linhas': '1000'
            }
        },
        stream=True  # read the response body as a stream
    )

    # raise an exception if the resturn status is 4XX or 5XX
    response.raise_for_status()

    rows = []
    print('Reading query results')
    for line in response.iter_lines():
        print(f'Reading row {line}')
        row = json.loads(line)
        rows.append(row)

    print(f'{len(rows)} rows successfully read!')


if __name__ == '__main__':
    run_query()
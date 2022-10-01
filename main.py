def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    final_dict = {}
    if '=' in query:
        ls = [i.replace('=', ' ', 1).split() for i in query.split(';')]
        ls1, ls2 = [], []
        for i in ls:
            if len(i) > 1:
                ls1.append(i[0])
                ls2.append(i[1])
        final_dict = dict(zip(ls1, ls2))
        return final_dict
    else:
        return final_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('age=33;name=Yaroslav') == {'age': '33', 'name': 'Yaroslav'}
    assert parse_cookie('growth=180;weight=80;') == {'growth': '180', 'weight': '80'}
    assert parse_cookie('growth=174') == {'growth': '174'}
    assert parse_cookie('name=Yaroslav=user=ubuntu') == {'name': 'Yaroslav=user=ubuntu'}
    assert parse_cookie('d') == {}
    assert parse_cookie('color=red') == {'color': 'red'}
    assert parse_cookie('taste=bitter;color=orange;') == {'taste': 'bitter', 'color': 'orange'}
    assert parse_cookie(';') == {}
    assert parse_cookie('class=mammals;row=1;') == {'class': 'mammals', 'row': '1'}
    assert parse_cookie('climate=subtropical=mediterranean;average-temperature=15,2;') == {'climate': 'subtropical=mediterranean', 'average-temperature': '15,2'}
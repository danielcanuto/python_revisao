#!/usr/bin/python3

def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        # pop retonra apenas o valor da chave
        kwargs['class'] = kwargs.pop("html_class")
    attrs = "".join(f'{k}="{v}" ' for k, v in kwargs.items())
    inner = "".join(args)

    return f'<{tag} {attrs}>{inner}</{tag}>'

if __name__ =="__main__":
    print(
        tag('p',
            tag("span", 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', 'e'),
            tag('Strong', 'Leonardo Leitão', id='ll'),
            tag('span','.'),
            html_class="alert"
        )
    )

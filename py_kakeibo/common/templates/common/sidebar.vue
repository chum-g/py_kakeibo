<!-- {% for cat, urls in link.items %}
    <p style="font-weight: bold; ">・{{cat}}</p>
    {% for name, url in urls.items %}
        <p style="text-indent: 1rem;"><a href={{index_url}}{{url}}>{{name}}</a></p>
    {% endfor %}
{% endfor %} -->

<p style="font-weight: bold; ">お知らせ</p>
    <p style="text-indent: 1rem;"><a href='/notification'>
        ・お知らせ一覧
    </a></p>

<p style="font-weight: bold; ">家計簿</p>
    <p style="text-indent: 1rem;"><a href='/detail/summary_year'> 
        ・年間集計
    </a></p>
    <p style="text-indent: 1rem;"><a href='/detail/summary_month'>
        ・月間集計
    </a></p>
    <p style="text-indent: 1rem;"><a href='/detail/index'>
        ・家計簿入力
    </a></p>

<p style="font-weight: bold; ">設定</p>
    <p style="text-indent: 1rem;"><a href=>
        ・ユーザー設定
    </a></p>
    
<p style="font-weight: bold; ">問い合わせ</p>
    <p style="text-indent: 1rem;"><a href=>
        ・問い合わせ
    </a></p>
    <p style="text-indent: 1rem;"><a href=>
        ・その他
    </a></p>
{{ item }}
<fieldset>
    <legend><h1>X月X日</h1></legend>
    <legend><h1>合計0円</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    <div>
        絞り込み:
        <select name="fillter">
            <option>選択肢のサンプル1</option>
            <option>選択肢のサンプル2</option>
            <option>選択肢のサンプル3</option>
        </select>
    </div>
    <div>
        並び順:
        <select name="sort">
            <option>選択肢のサンプル1</option>
            <option>選択肢のサンプル2</option>
            <option>選択肢のサンプル3</option>
        </select>
    </div>
    <div>
        <table border="1px">
            <tr><th>項目名</th><th>金額</th><th>備考</th><th>編集</th></tr>
            <tr><td>スタバ</td><td>2,000円</td><td>新作</td><td>[x]</td></tr>
            <tr><td>スタバ</td><td>2,000円</td><td>新作</td><td>[x]</td></tr>
        </table>
    </div>
    <!-- http://localhost:8000/kakeibo/2023/2/regist/　にアクセスする -->
    <form action="{% url 'detail:regist' 2023 2 %}" method="post">
        <!-- Djangoの機能　csrf対策 -->
        {% csrf_token %}
        <table border="1px">
            <tr><th>項目名</th><th>金額</th><th>備考</th></tr>
            <tr>
                <td><input id="" class="" type="text" value="項目名"></td>
                <td><input id="" class="" type="number" value="0"></td>
                <td><input id="" class="" type="text" value="備考"></td>
            </tr>
            <tr><td><input type="submit" value="regist"> </td></tr>
        </table>  
    </form>
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>

<div>
    <a href="/detail/{{date|date:"Y"}}/">年間集計</a>
</div>
<div>
    <a href="/detail/{{date|date:"Y"}}/{{date|date:"m"}}">月間集計</a>
</div>
<div>
    <a href="/notification/">お知らせ一覧</a>
</div>

<div>
    <a href="{{request.META.HTTP_REFERER}}">前のページに戻る</a>
</div>
<!DOCTYPE html>
{% extends "common/base.html" %}
{% block title_block %}
    ユーザ登録
{% endblock %}

{% block script_block %}
<script>
    let id = 0
    
    export default {
      data() {
        return {
          newTodo: '',
          hideCompleted: false,
          todos: [
            { id: id++, text: 'Learn HTML', done: true },
            { id: id++, text: 'Learn JavaScript', done: true },
            { id: id++, text: 'Learn Vue', done: false }
          ]
        }
      },
      computed: {
        // ...
      },
      methods: {
        addTodo() {
          this.todos.push({ id: id++, text: this.newTodo, done: false })
          this.newTodo = ''
        },
        removeTodo(todo) {
          this.todos = this.todos.filter((t) => t !== todo)
        }
      }
    }
    </script>
{% endblock %}

{% block body_block %}
    <!-- <h1>Welcome</h1> -->
    <h2>ユーザー登録</h2>
    <form method="POST" action="{% url 'login:signup' %}">
        {% csrf_token %}
        <label>ユーザー名</label>
        {{ form.username }}
        {{ form.username.errors }}
        <br>
        <label>パスワード</label>
        {{ form.password1 }}
        {{ form.password1.errors }}
        <br>
        <label>パスワード(確認)</label>
        {{ form.password2 }}
        {{ form.password2.errors }}
        <br>
        <input type="submit" value="登録する">
    </form>
    
{% endblock %}
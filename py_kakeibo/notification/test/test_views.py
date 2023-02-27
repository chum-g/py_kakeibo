from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

# from ..models import Post
from ..models import Notification


class LoggedInTestCase(TestCase):
  """各テストクラスで共通の事前準備処理をオーバーライド"""

  def setUp(self) -> None:
    """テストメソッド実行前の事前設定"""
    # テスト用アカウントの作成
    self.password = 'password123'
    self.test_user = get_user_model().objects.create_user(
      username='test_user',
      email='testuser@email.com',
      password=self.password
    )
    # テスト用アカウントをログインさせる
    self.client.login(username=self.test_user.username, email=self.test_user.email, password=self.password)


class TestNotificateCreate(LoggedInTestCase):
  """NotificateCreateのテスト"""
  def test_create_notificate_success(self):
    """記事作成の成功をテスト"""
    test_notification_id     = ''
    test_notification_title  = 'test_notificate_00'
    test_notification_detail = '本文'
    test_notification_start  = ''
    test_notification_end    = ''
    test_notification_from_user_id = ''
    test_notification_to_user_ids  = ''

    # お知らせデータを作成
    params = {
        'title': test_notification_title,
        'text' : test_notification_detail
        }
    Notification.objects.create(
        # notification_id     = '',
        notification_title  = 'test_notificate_00',
        notification_detail = '本文',
        notification_start  = '2023-01-01',
        notification_end    = '2024-01-01',
        notification_from_user_id = '0',
        notification_to_user_ids  = 'ALL',
        )
    # response = self.client.post(reverse_lazy('blog:post_create'), params)
    # 一覧ページへのリダイレクトを検証
    # self.assertRedirects(response, reverse_lazy('notification:/'))
    # データベースへ登録されたことを検証
    self.assertEqual(Notification.objects.filter(notification_title=test_notification_title).count(), 1)


# class TestPostCreate(LoggedInTestCase):
#   """PostCreateのテスト"""

#   def test_create_post_success(self):
#     """記事作成の成功をテスト"""
#     # 記事データを作成
#     params = {'title': 'テストタイトル',
#          'text': '本文'}
#     response = self.client.post(reverse_lazy('blog:post_create'), params)
#     # 一覧ページへのリダイレクトを検証
#     self.assertRedirects(response, reverse_lazy('blog:post_list'))
#     # データベースへ登録されたことを検証
#     self.assertEqual(Post.objects.filter(title='テストタイトル').count(), 1)

#   def test_create_post_failure(self):
#     """記事作成の失敗をテスト"""
#     # データを空で作成した場合の失敗を検証
#     response = self.client.post(reverse_lazy('blog:post_create'))
#     self.assertFormError(response, form='form', field='title', errors='このフィールドは必須です。')

#     # タイトルのみ入れた場合の失敗を検証
#     params = {'title': 'タイトル'}
#     response = self.client.post(reverse_lazy('blog:post_create'), params)
#     self.assertFormError(response, form='form', field='text', errors='このフィールドは必須です。')

#     # 本文のみ入れて作成した場合の失敗を検証
#     params = {'text': '本文'}
#     response = self.client.post(reverse_lazy('blog:post_create'), params)
#     self.assertFormError(response, form='form', field='title', errors='このフィールドは必須です。')

#     # ログアウトしている場合
#     self.client.logout()
#     params = {'title': 'ログアウトユーザー',
#          'text': '本文\n本文'}
#     response = self.client.post(reverse_lazy('blog:post_create'), params)
#     # ログインページへのリダイレクトを検証
#     self.assertRedirects(response, '/login/?next=/post_create/')
#     # データが追加されていないことを検証
#     self.assertEqual(Post.objects.filter(title='ログアウトユーザー').count
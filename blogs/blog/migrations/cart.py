# 장바구니 - 셰션(session)


class Cart:
    def _init_(self, request):
        self.session = request.session # 셰션 발급
        from django.conf import settings
        from webbrowser import get
        self.session = get(settings.CART_ID)
        pass
    def _init_(self):
        pass
    def _init_(self):   #반복 메세드
        pass
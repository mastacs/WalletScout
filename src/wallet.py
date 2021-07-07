class Wallet:

    def __init__(self, type, category, address, symbol, decimals, label, img, hide, canExchange, price, balance, balanceRaw, balanceUSD):
        self._type        = type
        self._category    = category
        self._address     = address
        self._symbol      = symbol
        self._decimals    = decimals
        self._label       = label
        self._img         = img
        self._hide        = hide
        self._canExchange = canExchange
        self._price       = price
        self._balance     = balance
        self._balanceRaw  = balanceRaw
        self._balanceUSD  = balanceUSD

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @type.deleter
    def type(self):
        del self._type

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @category.deleter
    def category(self):
        del self._category

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, addr):
        self._address = addr

    @address.deleter
    def address(self):
        del self._address

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @symbol.deleter
    def symbol(self):
        del self._symbol

    @property
    def decimals(self):
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        return self._decimals

    @decimals.deleter
    def decimals(self):
        del self._decimals

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @label.deleter
    def label(self):
        del self._label

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        self._img = img

    @img.deleter
    def img(self):
        del self._img

    @property
    def hide(self):
        return self._hide

    @hide.setter
    def hide(self, hide):
        self._hide = hide

    @property
    def canExchange(self):
        return self._canExchange

    @canExchange.setter
    def canExchange(self, canExchange):
        self._canExchange = canExchange

    @canExchange.deleter
    def canExchange(self):
        del self._canExchange

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @price.deleter
    def price(self):
        del self._price

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @balance.deleter
    def balance(self):
        del self._balance

    @property
    def balanceRaw(self):
        return self._balanceRaw

    @balanceRaw.setter
    def balanceRaw(self, balance):
        self._balanceRaw = balance

    @balanceRaw.deleter
    def balanceRaw(self):
        del self._balanceRaw

    @property
    def balanceUSD(self):
        return self._balanceUSD

    @balanceUSD.setter
    def balanceUSD(self, balance):
        self._balanceUSD = balance

    @balanceUSD.deleter
    def balanceUSD(self):
        del self._balanceUSD

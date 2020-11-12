import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5}, 'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanFindInvoiceClass():
    invoice = Invoice()

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalPurePrice(products):
    invoice = Invoice()
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateTotalDiscount(products):
    invoice = Invoice()
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62
#new method
def test_CanCalculateHalfDiscount(products):
    invoice = Invoice()
    invoice.partialDiscount(products)
    assert invoice.partialDiscount(products) == 2.81

#new method
def test_CanCalculateHalfPurePrice(products):
    invoice = Invoice()
    invoice.halfPurePrice(products)
    assert invoice.halfPurePrice(products) == 72.19

import decimal

from celery import shared_task


@shared_task
def debug_task(sleep_time: int = 5):
    from time import sleep
    sleep(sleep_time)
    print(f"задачу сделаль {sleep_time}")


@shared_task
def contact_us(subject, body):
    from django.conf import settings
    from django.core.mail import send_mail
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def debug_task2():
    from currency.models import Rate
    print(f'кол-во записей {Rate.objects.count()}')


@shared_task
def zdelal():
    print("задачу зделяль!")


@shared_task
def parse_privarbank():
    import requests
    from decimal import Decimal
    from currency.models import Rate2
    from currency import model_choises as MCH
    privatbank_currency_url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    responce = requests.get(privatbank_currency_url)
    responce.raise_for_status()
    rates2 = responce.json()
    source = "privatbank"
    currency_choise_type = {"USD": MCH.TYPE_USD, "EUR": MCH.TYPE_EUR}
    for i in rates2:
        if i["ccy"] in currency_choise_type:
            currency_type = i["ccy"]
            sale = Decimal(i["sale"]).quantize(
                Decimal(".01"))  # .1 - 1 знак после запятой, .01 - 2 знака после запятой, .001 - 3 знака после запятой
            buy = Decimal(i["buy"]).quantize(Decimal(".01"))
            lastrate2 = Rate2.objects.filter(
                type=currency_choise_type[currency_type],
                source=source
            ).order_by("created").last()
            if lastrate2 is None or lastrate2.sale != sale or lastrate2.buy != buy:
                Rate2.objects.create(
                    type=currency_choise_type[currency_type],
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parse_kurs_com_ua():
    from currency.models import Rate2
    from decimal import Decimal
    import requests
    from bs4 import BeautifulSoup
    URL = "https://kurs.com.ua/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table', attrs={'class': 'table-course negative-margin-767'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [i.text.strip() for i in cols]
        if cols[0] in ("USD", "EUR"):
            data.append({
                'type': cols[0],
                'buy': cols[1][:5],
                'sale': cols[2][:5]
            })
    source = "kurs.com.ua"
    for i in data:
        currency_type = i["type"]
        sale = Decimal(i["sale"]).quantize(Decimal(".01"))
        buy = Decimal(i["buy"]).quantize(Decimal(".01"))
        lastrate2 = Rate2.objects.filter(type=currency_type, source=source).order_by("created").last()
        if lastrate2 is None or lastrate2.sale != sale or lastrate2.buy != buy:
            Rate2.objects.create(
                type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_finance_i_ua():
    from currency.models import Rate2
    from decimal import Decimal
    import requests
    from bs4 import BeautifulSoup
    URL = "https://finance.i.ua/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table', attrs={'class': 'table table-data -important'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('th')
        cols2 = row.find_all('td')
        for i in cols2:
            cols.append(i)
        cols = [i.text.strip() for i in cols]
        if cols[0] in ("USD", "EUR"):
            data.append({
                'type': cols[0],
                'buy': cols[1][:5],
                'sale': cols[2][:5]
            })
    source = "finance.i.ua"
    for i in data:
        currency_type = i["type"]
        sale = Decimal(i["sale"]).quantize(Decimal(".01"))
        buy = Decimal(i["buy"]).quantize(Decimal(".01"))
        lastrate2 = Rate2.objects.filter(type=currency_type, source=source).order_by("created").last()
        if lastrate2 is None or lastrate2.sale != sale or lastrate2.buy != buy:
            Rate2.objects.create(
                type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )


@shared_task
def parse_minfin_com_ua():
    from currency.models import Rate2
    from decimal import Decimal
    import requests
    from bs4 import BeautifulSoup
    URL = "https://minfin.com.ua/currency/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table',
                      attrs={'class': 'table-response mfm-table mfcur-table-lg mfcur-table-lg-currency has-no-tfoot'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [i.text.strip() for i in cols]
        str_buy = ""
        for i in cols[1][:5]:
            if i == ",":
                str_buy += "."
            else:
                str_buy += i
        str_cols = "".join(cols[:2])
        str_cols2 = str_cols.split("/")[1]
        str_cols3 = str_cols2.split("\n")[-1][:5]
        str_sale = ""
        for i in str_cols3:
            if i == ",":
                str_sale += "."
            else:
                str_sale += i
        if cols[0] in ("USD", "EUR"):
            data.append({
                'type': cols[0],
                'buy': str_buy,
                'sale': str_sale
            })
    source = "minfin.com.ua"
    for i in data:
        currency_type = i["type"]
        sale = Decimal(i["sale"]).quantize(Decimal(".01"))
        buy = Decimal(i["buy"]).quantize(Decimal(".01"))
        lastrate2 = Rate2.objects.filter(type=currency_type, source=source).order_by("created").last()
        if lastrate2 is None or lastrate2.sale != sale or lastrate2.buy != buy:
            Rate2.objects.create(
                type=currency_type,
                sale=sale,
                buy=buy,
                source=source,
            )

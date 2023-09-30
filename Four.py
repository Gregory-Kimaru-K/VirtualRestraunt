import flet as ft

def main(page: ft.page):
    page.window_width = 500
    page.window_width = 850
    page.bgcolor = "white"

    InvoiceNumber = ft.TextField(label = "InvoiceNumber")
    TotalInvoiceAmount = ft.TextField(label = "Invoice Amount in Dollars")
    Tip = ft.TextField(label = "Tip Amount in Cents")
    TotalPaymentByCard = ft.TextField(label = "Amount received by Card")
    CardCharges = ft.TextField(label = "Card Service charges as a Percent")
    TotalPaymentCash = ft.TextField(label = "Total payment by cash")

    def calculateChange(f):
        In_Number = InvoiceNumber.value
        TIN = int(TotalInvoiceAmount.value)
        TotalTip = ((int(Tip.value)) / 100) if Tip.value else 0
        TPBC = int(TotalPaymentByCard.value) if TotalPaymentByCard.value else 0
        CC = int(CardCharges.value) if CardCharges.value else 0
        TPC = int(TotalPaymentCash.value) if TotalPaymentCash.value else 0

        change = (TPBC * ((100 - CC)/100) + TPC) - (TotalTip+TIN)

        if TPBC == 0 and TPC == 0:
            page.add(ft.Text("Please enter at least one payment amount (Card or Cash)."))
            return

        change = (TPBC * ((100 - CC) / 100) + TPC) - (TotalTip + TIN)

        if In_Number and TIN and TPBC is not None and CC is not None and TPC is not None:
            if change < 0:
                change = abs(change)
                page.add(ft.Text(f"Outstanding amount against Invoice number P001 and need to be paid by customer: {change:.2f}"))
            else:
                page.add(ft.Text(f"Change is: {change:.2f}"))
        else:
            page.add(ft.Text("Please enter all the required values."))

    submit_button = ft.ElevatedButton(text = "Calculate Change")

    submit_button.on_click = calculateChange

    page.add(InvoiceNumber)
    page.add(TotalInvoiceAmount)
    page.add(Tip)
    page.add(TotalPaymentByCard)
    page.add(CardCharges)
    page.add(TotalPaymentCash)
    page.add(submit_button)

ft.app(target = main)
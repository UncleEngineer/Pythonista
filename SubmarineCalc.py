import ui
import console

def Calc(sender):
	disc = 1 - (float(discount.text) / 100)
	calc = int(textfield.text) * 1000 * disc
	result.text = 'รวมทั้งหมด (ลดแล้ว {}%) {:,.2f} ล้านบาท'.format(discount.text, calc)
	#console.alert('Result', 'รวมทั้งหมด {:,d} บาท'.format(calc))

v = ui.load_view()

textfield = v['quantity'] #select text field	

discount = v['discount']

result = v['result']

v.present('sheet')

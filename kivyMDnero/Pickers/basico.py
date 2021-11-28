from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker

KV = '''
MDFloatLayout:

    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
	
	def show_time_picker(self):
	   time_dialog = MDTimePicker()
	   time_dialog.bind(time=self.get_time)
	   time_dialog.open()
	   def get_time(self, instance, time):
   	 	'''
    		The method returns the set time.

    		:type instance: <kivymd.uix.picker.MDTimePicker object>
    		:type time: <class 'datetime.time'>
    		'''

    		return time


Test().run()
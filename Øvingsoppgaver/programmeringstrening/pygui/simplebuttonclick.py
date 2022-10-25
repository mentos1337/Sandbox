import dearpygui.dearpygui as dpg

def callback_funksjon():
    print("du har trykket")


dpg.create_context()
dpg.create_viewport(title="Simple button click", width=600, height=400)

with dpg.window(no_title_bar=True,width=600,height=400):
    dpg.add_button(label="Trykk meg",width=80,height=80, callback=callback_funksjon)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
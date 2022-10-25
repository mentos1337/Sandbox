import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Elements", width=400, height=400)

def callback_funksjon():
    print("Button has been clicked")

with dpg.window(label="Content", width=600, height=400):
    dpg.add_text("This is a text")
    dpg.add_input_text(label="Input text here", width=200)
    dpg.add_input_int(label="Input int here", width=200)
    dpg.add_input_float(label="Input float here", width=200)
    dpg.add_button(label="klikk meg", callback=callback_funksjon)



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
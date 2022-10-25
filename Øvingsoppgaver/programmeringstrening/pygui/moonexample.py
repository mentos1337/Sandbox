import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Simple button click", width=600, height=400)

def calculate_weight():
    weight = dpg.get_value("vekt")
    vekt = weight / 9.807 * 1.622
    dpg.set_value("result",f"Result: {vekt}")


with dpg.window(no_title_bar=True,width=600,height=400, no_move=True):
    dpg.add_input_float(label="Your weight on earth", width=200, tag="vekt")
    dpg.add_button(label="Calculate moon weight", callback=calculate_weight, tag="Result")
    dpg.add_text("Result: ", tag="result")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
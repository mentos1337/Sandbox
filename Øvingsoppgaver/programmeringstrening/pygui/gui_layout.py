import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=400)

    #positioning
with dpg.window(no_title_bar=True, width=400, height=400):
    dpg.add_button(label="Indent example", indent=200)
    dpg.add_button(label="absolute position example", pos=(100, 300))
    #grouping
    with dpg.group(horizontal=True, width=200):
        dpg.add_button(label="group width")
        dpg.add_button(label="group width")
    with dpg.group(horizontal=True, width=120):
        dpg.add_button(label="group exmaple2")
        dpg.add_button(label="group example2")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=400)

with dpg.window(no_title_bar=True, width=400, height=400):
    with dpg.tab_bar():
        with dpg.tab(label="Første tab"):
            dpg.add_button(label="Test")
        with dpg.tab(label="Andre tab"):
            with dpg.group(horizontal=True):
                dpg.add_text("Input: ")
                dpg.add_button(label="Trykk meg")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
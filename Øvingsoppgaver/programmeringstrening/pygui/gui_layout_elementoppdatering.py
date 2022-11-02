import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="elements", width=590,height=400)


with dpg.window(no_title_bar=True, tag="window"):
    with dpg.child_window(width=-1,height=35):
        with dpg.group(horizontal=True):
            dpg.add_button(label="File")
            dpg.add_button(label="Edit")
            dpg.add_button(label="View")
            dpg.add_button(label="Navigate")
            dpg.add_button(label="Code")
            dpg.add_button(label="Refactor")
            dpg.add_button(label="Run")
            dpg.add_button(label="Tools")
            dpg.add_button(label="Git")
            dpg.add_button(label="Window")
            dpg.add_button(label="Help")
    with dpg.group(horizontal=True):
        with dpg.child_window(height=200, width=180):
            with dpg.tree_node(label="Forlesning_19"):
                    dpg.add_text("Pycharm.py")
                    dpg.add_text("Templates.py")
        with dpg.child_window(height=200, width=-1):
            dpg.add_input_text(multiline=True, width=-1,height=-1)
    with dpg.child_window(width=-1, height=-1):
        dpg.add_text("console")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)
dpg.start_dearpygui()
dpg.destroy_context()
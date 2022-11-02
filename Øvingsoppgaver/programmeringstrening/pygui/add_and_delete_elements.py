import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="elements", width=590,height=400)

def item_add():
    item_name = dpg.get_value("itemToAdd")
    dpg.add_text(item_name, parent="cw_list")

def item_delete():
    dpg.delete_item("cw_list", children_only=True)

with dpg.window(no_title_bar=True, tag="window"):
    with dpg.group(horizontal=True):
        dpg.add_text("Item name:")
        dpg.add_input_text(width=150, tag="itemToAdd")
        dpg.add_button(label="Add item",callback=item_add)
        dpg.add_button(label="Delete item",callback=item_delete)
    with dpg.child_window(width=-1,height=-1,tag="cw_list"):
        ""
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)
dpg.start_dearpygui()
dpg.destroy_context()
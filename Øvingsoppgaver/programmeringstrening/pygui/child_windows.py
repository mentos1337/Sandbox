from tkinter import Scrollbar
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=400)

with dpg.window(no_title_bar=True, width=400, height=400):
    with dpg.child_window(width=100, height=100):
        for x in range(10):
            dpg.add_button(label="knapp")
    dpg.add_text("outside of child window")
    with dpg.child_window(width=-1, height=-1):
        dpg.add_text("hello")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
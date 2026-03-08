def get_element_size(window_size, element_vw, element_vh):
    vwSize, vhSize = window_size.replace(" ", "").split("x")
    vwSize = int(vwSize)
    vhSize = int(vhSize)
    element_vw = int(element_vw.replace("vw", ""))
    element_vh = int(element_vh.replace("vh", ""))
    element_width = int(vwSize * (element_vw / 100))
    element_height = int(vhSize * (element_vh / 100))    

    return f"{element_width} x {element_height}"

#Test cases
print(get_element_size("1200 x 800", "50vw", "50vh"))
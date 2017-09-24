import numpy as np
import win32gui, win32ui, win32con, win32api
import cv2

def grab_frame(size=None):

    hwin = win32gui.GetDesktopWindow()

    if size:
        left, top, x, y  = size
        width= x - left + 1
        height= y - top +1

    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)



    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)


    signedIntsArray = bmp.GetBitmapBits(True)

    img = np.fromstring(signedIntsArray, dtype='uint8')

    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    img_res = cv2.resize(img, (480,270))
    img_rgb = cv2.cvtColor(img_res, cv2.COLOR_BGRA2RGB)
    #img_fl = np.array(list(img_rgb), dtype=np.float)
    return img_rgb

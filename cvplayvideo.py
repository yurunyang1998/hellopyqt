import cv2
import xmltest

drawing = False #鼠标按下为真
mode =  True#如果为真，画矩形，按m切换为曲线
ix,iy=1,10
TX,TY =1,10
trackbarname = 'bar'

VIDEO_DIR = r"D:\烟雾视频汇总\复杂场景中的烟雾\00403.avi"
img_path = 'D:/new_image/'

slider_postion = 0
videocapture = cv2.VideoCapture(VIDEO_DIR)
def ontrackbarslide(pos):
    videocapture.set(cv2.CAP_PROP_POS_FRAMES,pos)



def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,TX,TY
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                #tx,ty = x,y
                t = cv2.rectangle(frame,(ix,iy),(x,y),(0,255,0),0)

                cv2.imshow("pic0",t)

            else:
                cv2.circle(frame,(x,y),5,(0,0,255),0)
    elif event == cv2.EVENT_LBUTTONUP:
        TX,TY =x,y
        drawing = False
        if mode == True:
            #TX,TY = x,y
            #print(TX,TY)
            cv2.rectangle(frame,(ix,iy),(x,y),(0,255,0),0)
        else:
            #TX,TY = x,y
            cv2.circle(frame,(x,y),5,(0,0,255),0)






if __name__ == '__main__':
    tutol_frame_count = videocapture.get(cv2.CAP_PROP_FRAME_COUNT)

    #     #获得码率及尺
    fps = videocapture.get(cv2.CAP_PROP_FPS)
    size = [int(videocapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
               int(videocapture.get(cv2.CAP_PROP_FRAME_HEIGHT))]


        # 读帧
    success, frame = videocapture.read()
    cv2.namedWindow("pic0",0)
    cv2.createTrackbar("track",'pic0',0,int(tutol_frame_count),ontrackbarslide)
    i=0
    while success :
        if(i==1000):
            break


        image_save_path = img_path+str(i)+'.jpg'

        i=i+1

        cv2.namedWindow("pic0",flags=0)

        #cv2.namedWindow("roi",cv2.WINDOW_AUTOSIZE)
        cv2.imshow("pic0",frame)


        if(cv2.waitKey(1)>0):
            cv2.waitKey(-1)

        cv2.waitKey(int(1000/fps) ) #延迟
        success, frame = videocapture.read() #获取下一帧
        cv2.setMouseCallback('pic0',draw_circle)
        img = cv2.rectangle(frame,(ix,iy),(TX,TY),(0,255,0),0)
        xmltest.write_xml(str(i),image_save_path,str(size[0]),str(size[1]),str(3),"smoke",str(ix),str(iy),str(TX),str(TY),"D:\make_csv")

        img = frame

        if(cv2.imwrite(image_save_path,img)):

            cv2.imwrite(image_save_path,img)
        cv2.setTrackbarPos("track","pic0",int(videocapture.get(cv2.CAP_PROP_POS_FRAMES)))
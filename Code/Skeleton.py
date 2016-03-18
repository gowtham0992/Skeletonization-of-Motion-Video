

#For Video Output click the following link:  Input:  https://www.youtube.com/watch?v=LwixevNkjPE
#Output: https://www.youtube.com/watch?v=dbSNixzSGXU


import os
from skimage.morphology import skeletonize
from skimage import draw
import cv2
import scipy

# Converting an Video into multiple frames
i=0
path = "a.mp4"
video_object = cv2.VideoCapture(path)
directory = "frames"

if not os.path.exists(directory):
    os.makedirs(directory)

success = True
while success:
    success,frame = video_object.read()
    if success:
        cv2.imwrite(directory+"//"+path[:-4]+"_"+str(i).zfill(6)+".jpg",frame)
	i=i+1
print("Done!")

#finding the number of frames

file_list = os.listdir("./frames/")
file_list= sorted(file_list, key = lambda x: x.rsplit('.', 1)[0]) 
frame_count = len(file_list)
print file_list
out_dir = "skel_frame"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# performing skeletonization and saving it in an output file

for i in range(0,frame_count) :
	file_name = "./frames/"+file_list[i]
	#print file_name
	image= cv2.imread(file_name,0)
	img=cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
	im = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)[1]
	scipy.misc.imsave('a.jpg',im)
	im = cv2.bitwise_not(im)

	scipy.misc.imsave('b.jpg',im)
	skel = skeletonize(im > 0)
	scipy.misc.imsave('./'+out_dir+'/'+'img_'+str(i)+'.jpg',skel)

# Converting the frames into a video


os.system("ffmpeg -r 10 -b 800 -i ./skel_frame/img_%d.jpg video.mp4")


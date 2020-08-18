import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import glob
from camera import Camera
import structure
import processor
import features

def dino(a,b):
    # Dino
    #img1 = cv2.imread('imgs/dinos/viff.003.ppm')
    #img2 = cv2.imread('imgs/dinos/viff.001.ppm')
    img1 = cv2.imread(a)
    img2 = cv2.imread(b)
    pts1, pts2 = features.find_correspondence_points(img1, img2)
    points1 = processor.cart2hom(pts1)
    points2 = processor.cart2hom(pts2)

    height, width, ch = img1.shape
    intrinsic = np.array([  # for dino
        [2360, 0, width / 2],
        [0, 2360, height / 2],
        [0, 0, 1]])

    return points1, points2, intrinsic


points3d = np.empty((0,0))
files = glob.glob("imgs/dinos/*.ppm")
len = len(files)

for item in range(len-1):
    print(files[item], files[(item+1)%len])
    #dino() function takes 2 images as input
    #and outputs the keypoint point matches(corresponding points in two different views) along the camera intrinsic parameters.
    points1, points2, intrinsic = dino(files[item], files[(item+1)%len])
    #print(('Length', len(points1))
    # Calculate essential matrix with 2d points.
    # Result will be up to a scale
    # First, normalize points
    points1n = np.dot(np.linalg.inv(intrinsic), points1)
    points2n = np.dot(np.linalg.inv(intrinsic), points2)
    E = structure.compute_essential_normalized(points1n, points2n)
    print('Computed essential matrix:', (-E / E[0][1]))

    # Given we are at camera 1, calculate the parameters for camera 2
    # Using the essential matrix returns 4 possible camera paramters
    P1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
    P2s = structure.compute_P_from_essential(E)

    ind = -1
    for i, P2 in enumerate(P2s):
        # Find the correct camera parameters
        d1 = structure.reconstruct_one_point(
            points1n[:, 0], points2n[:, 0], P1, P2)

        # Convert P2 from camera view to world view
        P2_homogenous = np.linalg.inv(np.vstack([P2, [0, 0, 0, 1]]))
        d2 = np.dot(P2_homogenous[:3, :4], d1)

        if d1[2] > 0 and d2[2] > 0:
            ind = i

    P2 = np.linalg.inv(np.vstack([P2s[ind], [0, 0, 0, 1]]))[:3, :4]
    #tripoints3d = structure.reconstruct_points(points1n, points2n, P1, P2)
    tripoints3d = structure.linear_triangulation(points1n, points2n, P1, P2)

    if not points3d.size:
        print("sdsad")
        points3d = tripoints3d
    else:
        print(points3d.shape)
        points3d = np.concatenate((points3d, tripoints3d), 1)


fig = plt.figure()
fig.suptitle('3D reconstructed', fontsize=16)
ax = fig.gca(projection='3d')
print(points3d[0],points3d[0],points3d[0])
a1 = open('PuntosX.txt','w')
for i in points3d[0]:
    a1.write(str(i)+'\n')
a1.close()
a2 = open('PuntosY.txt','w')
for i in points3d[1]:
    a2.write(str(i)+'\n')
a2.close()
a3 = open('PuntosZ.txt','w')
for i in points3d[2]:
    a3.write(str(i)+'\n')
a3.close()
ax.plot(points3d[0], points3d[1], points3d[2], 'b.')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.view_init(elev=135, azim=90)
plt.show()

import math
import matplotlib.pyplot as plt
import numpy as np

# 角度の範囲
Theta = np.arange(20,45,2)
# Theta = [45]
# 速度の範囲
Vol = np.arange(15,25,0.5)
# Vol = 16

def fanc(t,v, x):
  # km/hからm/sに
  v = v*1000/(60*60)
  # 軌道の関数
  y = (math.tan(math.radians(t))*x) - (9.8*x*x/(2*v*v*math.cos(math.radians(t))*math.cos(math.radians(t))))
  # # m/sからkm/hに_実際このvは使ってない
  # v = v*(60*60)/1000
  return y

x_list = np.arange(0,2.44,0.01)
#描画エリアの作成
fig = plt.figure()
ax1 = fig.add_subplot(projection='3d')
for t in Theta:
  # 1つの角度θに対する軌道（複数）を描画
  for v in Vol:
    # 1つの速度vに対する軌道を描画
    ax1.plot(x_list,[v]*len(x_list),fanc(t,v,x_list),lw = 1)
    
# 3軸のラベル設定
ax1.set_xlabel("Distance(m)", size = 14)
ax1.set_ylabel("Speed(km/h)", size = 14)
ax1.set_zlabel("height(m)", size = 14)

plt.show()

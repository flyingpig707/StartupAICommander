"""Build the editable cover motif from the author-supplied compass concept."""
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
old = (root / 'book/public/assets/cover.svg').read_text()
start = old.index('<g opacity=".17">')
end = old.index('<path d="M86 1363H938"')
black, paper, accent = '#272724', '#f7f3e9', '#ef7b35'
segments = [
 ((515,1015),(438,908),(382,780),(310,786)),
 ((310,786),(250,792),(214,904),(130,1050)),
 ((130,1050),(60,1170),(65,1224),(203,1224)),
 ((203,1224),(252,1224),(300,1224),(348,1224)),
 ((348,1224),(422,1224),(438,1183),(481,1104)),
 ((481,1104),(510,1052),(548,984),(576,933)),
 ((576,933),(629,837),(698,791),(783,813)),
 ((783,813),(883,838),(930,912),(929,1015)),
 ((929,1015),(928,1126),(850,1211),(748,1218)),
 ((748,1218),(650,1226),(591,1133),(515,1015)),
]
def point(s,t):
 return tuple((1-t)**3*s[0][k]+3*(1-t)**2*t*s[1][k]+3*(1-t)*t*t*s[2][k]+t**3*s[3][k] for k in (0,1))
path = 'M515 1015 ' + ' '.join('C'+' '.join(f'{p[0]} {p[1]}' for p in s[1:]) for s in segments)+' Z'
parts = ['<path d="M103 790 C192 730 357 747 440 793 C521 838 569 777 710 763 C868 744 967 832 973 1003 C979 1155 915 1271 746 1276 C596 1280 533 1233 430 1267 C308 1306 137 1286 80 1205 C20 1122 45 905 103 790Z" fill="#e2ebe3"/>']
parts.append(f'<path d="{path}" fill="none" stroke="{black}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/>')
parts.append(f'<path d="{path}" fill="none" stroke="{paper}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
# Three ability stations sit exactly on the left-hand curve.
for t in (.18,.52,.9):
 x,y=point(segments[1],t)
 parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="16" fill="{paper}" stroke="{black}" stroke-width="4"/><circle cx="{x:.2f}" cy="{y:.2f}" r="10" fill="{accent}"/>')
# Ten decision nodes follow the right loop; omit the central crossing.
arc=[]
for s in segments[6:9]:
 for j in range(101):arc.append(point(s,j/100))
for j in range(61):arc.append(point(segments[9],j/100))
d=[0.0]
for a,b in zip(arc,arc[1:]): d.append(d[-1]+math.dist(a,b))
for i in range(10):
 target=d[-1]*(i+.18)/9.36
 k=min(range(len(d)), key=lambda k: abs(d[k]-target))
 x,y=arc[k]
 parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="10" fill="{paper}" stroke="{black}" stroke-width="4"/>')
parts += [
 '<text x="307" y="1045" text-anchor="middle" font-size="37" font-weight="650">九段进阶</text>',
 '<path d="M238 1064 Q302 1054 371 1059" stroke="#ef7b35" stroke-width="5" stroke-linecap="round" fill="none"/>',
 '<text x="307" y="1102" text-anchor="middle" font-size="19" fill="#62665f" letter-spacing="3">建立交付能力</text>',
 '<text x="746" y="1012" text-anchor="middle" font-size="37" font-weight="650">十步问道</text>',
 '<path d="M677 1031 Q745 1021 812 1026" stroke="#ef7b35" stroke-width="5" stroke-linecap="round" fill="none"/>',
 '<text x="746" y="1069" text-anchor="middle" font-size="19" fill="#62665f" letter-spacing="3">把生意走一遍</text>',
]
new = old[:start] + '\n'.join(parts)+'\n'+old[end:]
new = new.replace('暖白墨黑朱红封面，两条路径交汇，九级阶梯与十个节点。','AI指挥官罗盘：左侧三阶九段轨道，右侧十步决策环，交汇为无限循环；暖白、墨黑、朱红与浅青绿。')
# Replace the small bottom-right stair mark with a tiny compass/infinity mark.
new = new.replace('<path d="M900 1437v-11h9v-10h9v-7h9" fill="none" stroke="#f7f3e9" stroke-width="3"/>','<path d="M914 1425C906 1411 897 1419 900 1427C903 1436 909 1433 914 1425C920 1415 928 1418 928 1425C928 1435 919 1435 914 1425Z" fill="none" stroke="#f7f3e9" stroke-width="2.5"/>')
(root/'design/studies/cover-compass-vector-study.svg').write_text(new)
print('Saved editable vector study, not the generated cover master')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='DejaVu Sans'
INK='#1f2933'; GREY='#6b7280'; BLUE='#3b5ba9'; AMB='#b7791f'
rules=['use-of-md5-\ndigest-utils','use-of-md5','weak-random','md5-used-as-\npassword']
own=[1,3,3,1]; md5=[0,0,0,0]
causes=['call is in the file,\nbut in variable form','no getInstance call\nin the file','Random appears only\nas a type','no getInstance call\nin the file']
fig,ax=plt.subplots(figsize=(7.2,3.5),dpi=220)
x=range(4); w=0.36
b1=ax.bar([i-w/2 for i in x],own,w,color=BLUE,label='Findings on the rule’s own test file')
b2=ax.bar([i+w/2 for i in x],md5,w,color=AMB,label='Findings on Md5Crypt.java')
for i,(o,m) in enumerate(zip(own,md5)):
    ax.text(i-w/2,o+0.07,str(o),ha='center',fontsize=8,color=INK)
    ax.text(i+w/2,m+0.07,str(m),ha='center',fontsize=8,color=INK)
    ax.text(i,-1.05,causes[i],ha='center',va='top',fontsize=6.8,color=GREY)
ax.set_xticks(list(x)); ax.set_xticklabels(rules,fontsize=7.4,color=INK)
ax.tick_params(axis='x',pad=2)
ax.set_ylim(0,3.8); ax.set_yticks([0,1,2,3]); ax.set_ylabel('Findings (count)',fontsize=8,color=INK)
ax.tick_params(axis='y',labelsize=8)
for s in ['top','right']: ax.spines[s].set_visible(False)
ax.legend(fontsize=7.2,frameon=False,loc='upper right')
fig.subplots_adjust(bottom=0.36,top=0.95,left=0.09,right=0.98)
fig.text(0.09,0.02,'Cause under each rule, as read from the checks. Not a recall figure.',fontsize=6.8,color=GREY)
fig.savefig('figure_3_rule_results_2026-11-05.png')

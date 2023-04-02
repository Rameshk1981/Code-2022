#"""  

#Purpose: Creates Abaqus model (RVE3DParticulates) using inputs 
#******************************************************************************************************** 
#"""  


#Import Abaqus-related (Python) Object files 
from abaqus import * 
from abaqusConstants import * 
import __main__ 
import section 
import regionToolset 
import displayGroupMdbToolset as dgm 
import part 
import material 
import assembly 
import step 
import interaction 
import load 
import mesh 
import job 
import sketch 
import visualization 
import xyPlot 
import displayGroupOdbToolset as dgo 
import connectorBehavior 

#Create Viewport 
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=360) 
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints 
s1.setPrimaryObject(option=STANDALONE) 
#**************************************************** 
# MATRIX SECTION 
#**************************************************** 

#Sketch RVE window 
s1.rectangle(point1=(0.0,0.0), point2=(120, 120)) 
p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=THREE_D,type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Matrix']
p.BaseSolidExtrude(sketch=s1, depth=120)
s1.unsetPrimaryObject() 
p = mdb.models['Model-1'].parts['Matrix'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p) 
#**************************************************** 
# Ellipsoidal_PARTICULATES SECTION 
#**************************************************** 

del mdb.models['Model-1'].sketches['__profile__'] 
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=120) 
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints 
s.setPrimaryObject(option=STANDALONE) 
s.ConstructionLine(point1=(-120, 0.0), point2=(120, 0.0)) 
s.FixedConstraint(entity=g[2]) 
s.EllipseByCenterPerimeter(center=(0.0, 0.0), axisPoint1=(20, 0.0), axisPoint2=(0.0, 10)) 
s.Line(point1=(-20, 0.0), point2=(20, 0.0)) 
s.autoTrimCurve(curve1=g[3], point1=(-0.0, 10)) 
p = mdb.models['Model-1'].Part(name='Ellipsoid', dimensionality=THREE_D,
   type=DEFORMABLE_BODY) 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF) 
s.unsetPrimaryObject() 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p) 
del mdb.models['Model-1'].sketches['__profile__'] 
mdb.models['Model-1'].Material(name='SiliconCarbide') 
mdb.models['Model-1'].materials['SiliconCarbide'].Elastic(table=((410000000000,0.14),)) 
mdb.models['Model-1'].Material(name='Aluminium') 
mdb.models['Model-1'].materials['Aluminium'].Elastic(table=((75000000000,0.3),)) 
mdb.models['Model-1'].materials['Aluminium'].Plastic(scaleStress=None, 
    table=(
     (250000000, 0), 
     (248000000, 0.05), 
     (240000000, 0.15), 
     (230000000, 0.8), 
     (220000000, 1.5))) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Inclusions', 
 		 material='SiliconCarbide', thickness=None) 
mdb.models['Model-1'].HomogeneousSolidSection(name='Matrix', 
 		 material='Aluminium', thickness=None) 
#  
# ASSIGNMENT OF SECTIONS PART OF THE SCRIPT 
#  
p = mdb.models['Model-1'].parts['Ellipsoid'] 
c = p.cells 
cells = c.getSequenceFromMask(mask=('[#1 ]', ), ) 
region = regionToolset.Region(cells=cells) 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
p.SectionAssignment(region=region, sectionName='Inclusions', offset=0.0,
	 offsetType=MIDDLE_SURFACE, offsetField='',
	 thicknessAssignment=FROM_SECTION) 
p = mdb.models['Model-1'].parts['Matrix'] 
c = p.cells 
cells = c.getSequenceFromMask(mask=('[#1 ]', ), ) 
region = regionToolset.Region(cells=cells) 
p = mdb.models['Model-1'].parts['Matrix'] 
p.SectionAssignment(region=region, sectionName='Matrix', offset=0.0,
	 offsetType=MIDDLE_SURFACE, offsetField='',
	 thicknessAssignment=FROM_SECTION) 
a = mdb.models['Model-1'].rootAssembly 
session.viewports['Viewport: 1'].setValues(displayedObject=a) 
a1 = mdb.models['Model-1'].rootAssembly 
a1.DatumCsysByDefault(CARTESIAN) 
p = mdb.models['Model-1'].parts['Matrix'] 
a1.Instance(name='Matrix-1', part=p, dependent=ON) 
# ------------------------------------------------------------------- 
#Create  exact number of PARTICULATE instances 
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-1', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-2', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-3', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-4', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-5', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-6', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-7', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-8', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-9', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-10', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-11', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-12', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-13', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-14', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-15', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-16', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-17', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-18', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-19', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-20', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-21', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-22', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-23', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-24', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-25', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-26', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-27', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
p = mdb.models['Model-1'].parts['Ellipsoid'] 
a1.Instance(name='Ellipsoid-28', part=p, dependent=ON)
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-1', ), vector=(68.9593,81.4214,88.6368))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-2', ), vector=(70.3184,29.6081,79.9699))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-3', ), vector=(10.0179,75.1152,79.3133))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-4', ), vector=(87.5702,106.8903,117.8764))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-5', ), vector=(5.9439,58.7484,23.1012))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-6', ), vector=(22.6887,5.1183,76.2238))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-7', ), vector=(24.7171,113.752,9.8485))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-8', ), vector=(62.6263,40.3019,21.0803))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-9', ), vector=(71.753,94.7237,44.1184))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-10', ), vector=(114.8861,31.8386,110.9497))
a1 = mdb.models['Model-1'].rootAssembly 
#  
# TRANSLATE PERIODICALLY-CONSTRAINED PARTICULATES 
#  
a1.translate(instanceList=('Ellipsoid-11', ), vector=(130.0179,75.1152,79.3133))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-12', ), vector=(87.5702,-13.1097,117.8764))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-13', ), vector=(87.5702,106.8903,-2.1236))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-14', ), vector=(87.5702,-13.1097,117.8764))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-15', ), vector=(87.5702,-13.1097,-2.1236))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-16', ), vector=(87.5702,106.8903,-2.1236))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-17', ), vector=(125.9439,58.7484,23.1012))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-18', ), vector=(22.6887,125.1183,76.2238))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-19', ), vector=(24.7171,-6.248,9.8485))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-20', ), vector=(24.7171,113.752,129.8485))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-21', ), vector=(24.7171,113.752,129.8485))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-22', ), vector=(24.7171,-6.248,129.8485))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-23', ), vector=(24.7171,-6.248,9.8485))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-24', ), vector=(-5.1139,31.8386,110.9497))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-25', ), vector=(114.8861,31.8386,-9.0503))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-26', ), vector=(114.8861,31.8386,-9.0503))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-27', ), vector=(-5.1139,31.8386,-9.0503))
a1 = mdb.models['Model-1'].rootAssembly 
a1.translate(instanceList=('Ellipsoid-28', ), vector=(-5.1139,31.8386,110.9497))
a1 = mdb.models['Model-1'].rootAssembly 
a1.InstanceFromBooleanMerge(name='Composite', instances=( 
a1.instances['Matrix-1'], a1.instances['Ellipsoid-1'],
	 a1.instances['Ellipsoid-2'],
	 a1.instances['Ellipsoid-3'],
	 a1.instances['Ellipsoid-4'],
	 a1.instances['Ellipsoid-5'],
	 a1.instances['Ellipsoid-6'],
	 a1.instances['Ellipsoid-7'],
	 a1.instances['Ellipsoid-8'],
	 a1.instances['Ellipsoid-9'],
	 a1.instances['Ellipsoid-10'],
	 a1.instances['Ellipsoid-11'],
	 a1.instances['Ellipsoid-12'],
	 a1.instances['Ellipsoid-13'],
	 a1.instances['Ellipsoid-14'],
	 a1.instances['Ellipsoid-15'],
	 a1.instances['Ellipsoid-16'],
	 a1.instances['Ellipsoid-17'],
	 a1.instances['Ellipsoid-18'],
	 a1.instances['Ellipsoid-19'],
	 a1.instances['Ellipsoid-20'],
	 a1.instances['Ellipsoid-21'],
	 a1.instances['Ellipsoid-22'],
	 a1.instances['Ellipsoid-23'],
	 a1.instances['Ellipsoid-24'],
	 a1.instances['Ellipsoid-25'],
	 a1.instances['Ellipsoid-26'],
	 a1.instances['Ellipsoid-27'],
	 a1.instances['Ellipsoid-28'],
 ), keepIntersections=ON, 
 originalInstances=SUPPRESS, domain=GEOMETRY) 
#  
# EXTRUDE CUTTING SECTION 
#--------------------------------------------------------------------------------------
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
	engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues( 
	 referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Composite'] 
session.viewports['Viewport: 1'].setValues(displayedObject=p) 
#
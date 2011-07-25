# slicer imports
from __main__ import vtk, slicer

# python includes
import sys
import time

class Helper( object ):
  '''
  classdocs
  '''

  @staticmethod
  def Info( message ):
    '''
    
    '''

    print "[ChangeTrackerPy " + time.strftime( "%m/%d/%Y %H:%M:%S" ) + "]: " + str( message )
    sys.stdout.flush()

  @staticmethod
  def Warning( message ):
    '''
    
    '''

    print "[ChangeTrackerPy " + time.strftime( "%m/%d/%Y %H:%M:%S" ) + "]: WARNING: " + str( message )
    sys.stdout.flush()

  @staticmethod
  def Error( message ):
    '''
    
    '''

    print "[ChangeTrackerPy " + time.strftime( "%m/%d/%Y %H:%M:%S" ) + "]: ERROR: " + str( message )
    sys.stdout.flush()


  @staticmethod
  def Debug( message ):
    '''
    
    '''

    showDebugOutput = 1
    from time import strftime
    if showDebugOutput:
        print "[ChangeTrackerPy " + time.strftime( "%m/%d/%Y %H:%M:%S" ) + "] DEBUG: " + str( message )
        sys.stdout.flush()

  @staticmethod
  def CreateSpace( n ):
    '''
    '''
    spacer = ""
    for s in range( n ):
      spacer += " "

    return spacer


  @staticmethod
  def GetNthStepId( n ):
    '''
    '''
    steps = [None, # 0
             'SelectScans', # 1
             'DefineROI', # 2
             'SegmentROI', # 3
             'AnalyzeROI', # 4
             'ReportROI', # 5
             ]                        

    if n < 0 or n > len( steps ):
      n = 0

    return steps[n]

  @staticmethod
  def SetBgFgVolumes(bg, fg):
    appLogic = slicer.app.mrmlApplicationLogic()
    selectionNode = appLogic.GetSelectionNode()
    selectionNode.SetReferenceActiveVolumeID(bg)
    selectionNode.SetReferenceSecondaryVolumeID(fg)
    appLogic.PropagateVolumeSelection()
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file AddObject.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
from random import random
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
addobject_spec = ["implementation_id", "AddObject", 
         "type_name",         "AddObject", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "arai", 
         "category",          "test", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class AddObject
# @brief ModuleDescription
# 
# 
# </rtc-template>
class AddObject(OpenRTM_aist.DataFlowComponentBase):
 
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_In_voice = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._In_voiceIn = OpenRTM_aist.InPort("In_voice", self._d_In_voice)
        self._d_In_image = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._In_imageIn = OpenRTM_aist.InPort("In_image", self._d_In_image)
        self._d_In_VoiceSeq = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._In_VoiceSeqIn = OpenRTM_aist.InPort("In_VoiceSeq", self._d_In_VoiceSeq)
        self._d_In_imageSeq = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._In_imageSeqIn = OpenRTM_aist.InPort("In_imageSeq", self._d_In_imageSeq)
        self._d_In_PositionSeq = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._In_PositionSeqIn = OpenRTM_aist.InPort("In_PositionSeq", self._d_In_PositionSeq)
        self._d_Out_VoiceSeq = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._Out_VoiceSeqOut = OpenRTM_aist.OutPort("Out_VoiceSeq", self._d_Out_VoiceSeq)
        self._d_Out_ImageSeq = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._Out_ImageSeqOut = OpenRTM_aist.OutPort("Out_ImageSeq", self._d_Out_ImageSeq)
        self._d_Out_PositionSeq = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._Out_PositionSeqOut = OpenRTM_aist.OutPort("Out_PositionSeq", self._d_Out_PositionSeq)


  


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
  
        # </rtc-template>


   
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
  
        # Set InPort buffers
        self.addInPort("In_voice",self._In_voiceIn)
        self.addInPort("In_image",self._In_imageIn)
        self.addInPort("In_VoiceSeq",self._In_VoiceSeqIn)
        self.addInPort("In_imageSeq",self._In_imageSeqIn)
        self.addInPort("In_PositionSeq",self._In_PositionSeqIn)
  
        # Set OutPort buffers
        self.addOutPort("Out_VoiceSeq",self._Out_VoiceSeqOut)
        self.addOutPort("Out_ImageSeq",self._Out_ImageSeqOut)
        self.addOutPort("Out_PositionSeq",self._Out_PositionSeqOut)
  
        # Set service provider to Ports
  
        # Set service consumers to Ports
  
        # Set CORBA Service Ports
  
        return RTC.RTC_OK
 
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
 
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
 
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
 
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
 
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
        

            
            

        return RTC.RTC_OK
 
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        # 追加音声が来た場合
        if self._In_voiceIn.isNew():
            print("true")

            # 追加音声、画像を読み取る
            image_data = self._In_imageIn.read().data
            voice_data = self._In_voiceIn.read().data

            # 現在の音声配列、画像配列、座標配列のデータを読み取る
            imageSeq_data = list(self._In_imageSeqIn.read().data)
            voiceSeq_data = list(self._In_VoiceSeqIn.read().data)
            positionSeq_data = list(self._In_PositionSeqIn.read().data)

            # 確認用
            ################################################
            for data in imageSeq_data:
                print("before", data)

            for data in positionSeq_data:
                print("before", data)
            ################################################

            # 画像データ、音声データ、配列データ（0、0）をそれぞれの配列に追加する
            imageSeq_data.append(image_data)
            voiceSeq_data.append(voice_data)
            positionSeq_data.extend([0, 0])  # x座標、y座標

            # 確認用
            ################################################
            for data in imageSeq_data:
                print("after", data)

            for data in positionSeq_data:
                print("after", data)
            ################################################

            # データを一つずつ送信
            for data in voiceSeq_data:
                Outvoice = RTC.TimedOctetSeq(RTC.Time(0, 0), data)
                self._Out_VoiceSeqOut.write(Outvoice)

            for data in imageSeq_data:
                Outimage = RTC.TimedOctetSeq(RTC.Time(0, 0), data)
                self._Out_ImageSeqOut.write(Outimage)

            for i in range(0, len(positionSeq_data), 2):
                Outposition = RTC.TimedShortSeq(RTC.Time(0, 0), positionSeq_data[i:i+2])
                self._Out_PositionSeqOut.write(Outposition)

        return RTC.RTC_OK
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
 
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
 
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
 
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
 
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
 



def AddObjectInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=addobject_spec)
    manager.registerFactory(profile,
                            AddObject,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    AddObjectInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("AddObject" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()
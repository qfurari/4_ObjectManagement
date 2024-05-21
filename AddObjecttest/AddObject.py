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
import pyaudio


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
    def play_audio(self,data):
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(2),  # フォーマットを指定
                        channels=1,                         # モノラル
                        rate=44100,                         # サンプリングレート
                        output=True)                        # 出力用ストリームとして開く

        stream.write(data)  # バイナリデータを再生

        stream.stop_stream()
        stream.close()
        p.terminate()
    


    def onExecute(self, ec_id):
        #追加画像が来た場合(実際に使うとき)
        if self._In_voiceIn.isNew():
        #############################
        #確認用ー座標配列が来た場合
        #if self._In_PositionSeqIn.isNew():
        #############################
            imageSeq_data=[]
            voiceSeq_data=[]
            positionSeq_data=[]

            #追加
            #音声、画像を読み取る
            image_data=self._In_imageIn.read().data
            voice_data=self._In_voiceIn.read().data

            #確認用（voice)
            #########################################
            #音声再生
            self.play_audio(voice_data)
            #########################################

            
            #現在の音声配列、画像配列、座標配列のデータを読み取る
            imageSeq_data=self._In_imageSeqIn.read().data
            voiceSeq_data=self._In_VoiceSeqIn.read().data
            positionSeq_data=self._In_PositionSeqIn.read().data

            #確認用(座標)
            ################################################
            #for data in positionSeq_data:
            #    print("追加前の座標要素",data)
            ################################################

            #確認用(voice)
            ################################################
            for data in voiceSeq_data:
                print("追加前のvoice要素",data)
            ################################################

            position_new=[]

            #画像データ、音声データ,配列データ（０、０）をそれぞれの配列に追加する
            imageSeq_data.append(image_data)
            voiceSeq_data.append(voice_data)
            position_new.append(0)#x座標
            position_new.append(0)#y座標
            positionSeq_data.append(positionSeq_data)

            print("追加後の音声",voiceSeq_data[0])
            #確認用
            ################################################
            #for data in positionSeq_data:
            #   print("追加後の座標要素",data)
            ################################################
            #確認用
            ################################################
            #for data in voiceSeq_data:
            #   print("追加後のvoice要素",data)
            ################################################
            #確認用（voice)
            #########################################
            #音声再生
            self.play_audio(voiceSeq_data[0])
            #########################################


            #画像データ、音声データは型をTimedOctedSeqに変更       
            Outvoice=RTC.TimedOctedSeq(RTC.Time(0, 0), voiceSeq_data)
            #Outimage=RTC.TimedOctedSeq(RTC.Time(0, 0), imageSeq_data)
            #座標データは型をTimedShortSeqに変換
            Outposition = RTC.TimedShortSeq(RTC.Time(0, 0), positionSeq_data)

            #OutPortでそれぞれの配列を出力
            self._Out_VoiceSeqOut.write(Outvoice)
            #self._Out_ImageSeqOut.write(Outimage)
            #self._Out_PositionSeqOut.write(Outposition)

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


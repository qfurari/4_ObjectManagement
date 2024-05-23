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
sys.path.append(".")
# Import RTM module
import RTC
import OpenRTM_aist
# This module's specification
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
class AddObject(OpenRTM_aist.DataFlowComponentBase):
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
        self._d_In_voice = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        self._In_voiceIn = OpenRTM_aist.InPort("In_voice", self._d_In_voice)
        self._d_In_analysis = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        self._In_analysis = OpenRTM_aist.InPort("In_analysis", self._d_In_analysis)
        self._d_In_VoiceSeq = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        self._In_VoiceSeqIn = OpenRTM_aist.InPort("In_VoiceSeq", self._d_In_VoiceSeq)
        self._d_In_analysisSeq = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        self._In_imageSeqIn = OpenRTM_aist.InPort("In_imageSeq", self._d_In_analysisSeq)
        self._d_In_PositionSeq = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        self._In_PositionSeqIn = OpenRTM_aist.InPort("In_PositionSeq", self._d_In_PositionSeq)
        self._d_Out_VoiceSeq = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        self._Out_VoiceSeqOut = OpenRTM_aist.OutPort("Out_VoiceSeq", self._d_Out_VoiceSeq)
        self._d_Out_analysisSeq = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        self._Out_analysisSeqOut = OpenRTM_aist.OutPort("Out_analysisSeq", self._d_Out_analysisSeq)
        self._d_Out_PositionSeq = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        self._Out_PositionSeqOut = OpenRTM_aist.OutPort("Out_PositionSeq", self._d_Out_PositionSeq)
    def onInitialize(self):
        self.addInPort("In_voice", self._In_voiceIn)
        self.addInPort("In_analysis", self._In_analysis)
        self.addInPort("In_VoiceSeq", self._In_VoiceSeqIn)
        self.addInPort("In_imageSeq", self._In_imageSeqIn)
        self.addInPort("In_PositionSeq", self._In_PositionSeqIn)
        self.addOutPort("Out_VoiceSeq", self._Out_VoiceSeqOut)
        self.addOutPort("Out_analysisSeq", self._Out_analysisSeqOut)
        self.addOutPort("Out_PositionSeq", self._Out_PositionSeqOut)
        return RTC.RTC_OK
    def onActivated(self, ec_id):
        return RTC.RTC_OK
    def onDeactivated(self, ec_id):
        return RTC.RTC_OK
    def onExecute(self, ec_id):
        import random
        if self._In_voiceIn.isNew():
            print("true")
            voiceSeq_data=[]
            positionSeq_data=[]
            analysisSeq_data=[]
            analysis_data = self._In_analysis.read().data
            voice_data = self._In_voiceIn.read().data
            print(f"analysis{analysis_data}")
            #座標データを１組ずつ受け取ってリストに格納する
            if self._In_PositionSeqIn.isNew():
                while self._In_PositionSeqIn.isNew():
                    xy_data=self._In_PositionSeqIn.read().data
                    for i in range (0,len(xy_data),2):
                        positionSeq_data.append((xy_data[i],xy_data[i+1]))
                    print(F"Resived position_Data{positionSeq_data}")
            #追加analysisデータを配列に格納する
            if self._In_imageSeqIn.isNew():
                analysisSeq_data = self._In_analysisSeqIn.read().data
                print(f"Resived analysis_data{analysisSeq_data}")
            #音声データを一つずつ受け取ってリストに格納する
            if self._In_VoiceSeqIn.isNew():
                while self._In_VoiceSeqIn.isNew():
                    voice_data=self._In_VoiceSeqIn.read().data
                    voiceSeq_data.append(voice_data)
                    print(F"Resived position_Data{voiceSeq_data}")
            #追加データの追加
            analysisSeq_data.append(analysis_data)
            voiceSeq_data.append(voice_data)
            # ランダムな座標を生成して追加
            random_x = random.randint(1, 100)
            random_y = random.randint(1, 100)
            positionSeq_data.extend([random_x, random_y])
            for data in voiceSeq_data:
                Outvoice = RTC.TimedOctetSeq(RTC.Time(0, 0), data)
                self._Out_VoiceSeqOut.write(Outvoice)
            Outanalysis = RTC.TimedShortSeq(RTC.Time(0, 0), analysisSeq_data)
            self._Out_analysisSeqOut.write(Outanalysis)
            for i in range(0, len(positionSeq_data), 2):
                Outposition = RTC.TimedShortSeq(RTC.Time(0, 0), positionSeq_data[i:i+2])
                self._Out_PositionSeqOut.write(Outposition)
        return RTC.RTC_OK
def AddObjectInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=addobject_spec)
    manager.registerFactory(profile, AddObject, OpenRTM_aist.Delete)
def MyModuleInit(manager):
    AddObjectInit(manager)
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
    comp = manager.createComponent("AddObject" + args)
def main():
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()
if __name__ == "__main__":
    main()
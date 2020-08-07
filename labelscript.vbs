'	b-PAC 3.0 Component Sample (Instant Name Plate)
'	(C)Copyright Brother Industries, Ltd. 2009
'
'<SCRIPT LANGUAGE="VBScript">
	' Data Folder
	Const sDataFolder = "D:\labelprint\"
	DoPrint(sDataFolder & "label.lbx")

	'*******************************************************************
	'	Print Module
	'*******************************************************************
	Sub DoPrint(strFilePath)
		Set ObjDoc = CreateObject("bpac.Document")
		bRet = ObjDoc.Open(strFilePath)
		If (bRet <> False) Then
			ObjDoc.GetObject("AssetName").Text = "$ANAME"
			ObjDoc.GetObject("AssetTag").Text = "$ATAG"
                        ObjDoc.GetObject("company").Text = "Villa College"
                        
                        Call ObjDoc.SetBarcodeData(ObjDoc.GetBarcodeIndex("QR"), "$ALINK")

			' ObjDoc.SetMediaByName ObjDoc.Printer.GetMediaName(), True
			ObjDoc.StartPrint "", 0
			ObjDoc.PrintOut 1, 0
			ObjDoc.EndPrint
			ObjDoc.Close
		End If
		Set ObjDoc = Nothing
	End Sub

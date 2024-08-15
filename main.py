Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices

Module Module1
    Sub Main()
        ' SolidWorks application instance
        Dim swApp As SldWorks = Nothing
        swApp = CType(Marshal.GetActiveObject("SldWorks.Application"), SldWorks)

        ' Open file dialog to select a .slddrw file
        Dim openFileDialog As New OpenFileDialog()
        openFileDialog.Filter = "SolidWorks Drawing Files (*.slddrw)|*.slddrw"
        If openFileDialog.ShowDialog() = DialogResult.OK Then
            Dim filePath As String = openFileDialog.FileName

            ' Open the selected drawing document
            Dim swDoc As ModelDoc2 = swApp.OpenDoc(filePath, swDocumentTypes_e.swDocDRAWING)
            If swDoc Is Nothing Then
                Console.WriteLine("Dosya açılamadı.")
                Return
            End If

            ' Cast to drawing document
            Dim swDrawing As DrawingDoc = CType(swDoc, DrawingDoc)
            If swDrawing Is Nothing Then
                Console.WriteLine("Geçersiz bir .slddrw dosyası.")
                Return
            End If

            ' Get the number of views
            Dim viewCount As Integer = swDrawing.GetViewCount()

            ' Output the view count
            Console.WriteLine("Görünüm Sayısı: " & viewCount)

            ' Close the document
            swApp.CloseDoc(filePath)
        Else
            Console.WriteLine("Dosya seçimi iptal edildi.")
        End If

        Console.WriteLine("Program sona erdi. Çıkmak için bir tuşa basın...")
        Console.ReadKey()
    End Sub
End Module

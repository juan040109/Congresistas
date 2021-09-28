import sys
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from congrasistas import clase_congrasistas

import asistencia_congreso as mod

class aplicacion_congrasistas(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = clase_congrasistas()
        self.dialogo.setupUi(self)
        self.dialogo.btn_Cerrar.clicked.connect(self.examinar)
        self.dialogo.btn_Aceptar.clicked.connect(self.Aceptar)
        self.show()
    def examinar(self):
        self.archivo = QFileDialog.getOpenFileName(self,'abrir archivo','C:\\','Text files()')
        print(self.archivo[0])
    
    def Aceptar(self):

        archivo = mod.cargar_datos(self.archivo[0])


        if self.dialogo.rbt_opcion1.isChecked() == True:
            nombre,cantidad = mod.mas_asistencias(archivo)
            self.dialogo.lbl_resultado.setText(
            '''El congresista 
        {}
                asistio {} veces
                   a sesiones'''.format(nombre,cantidad))

        if self.dialogo.rbt_opcion2.isChecked() == True:
            mas_asistencia,asitio = mod.mas_asistencias(archivo)
            self.dialogo.lbl_resultado.setText(
            '''El congresista 
            {} 
              asistió {} veces 
              a sesiones de la 
              Cámara de Representantes'''.format(mas_asistencia,asitio))

        if self.dialogo.rbt_opcion3.isChecked() == True:
            resultado = mod.porcentaje_asistencias(archivo)
            print(resultado)
            self.dialogo.lbl_resultado.setText('{}'.format(resultado))

        if self.dialogo.rbt_opcion4.isChecked() == True:
            resultado = 'hola4'
            self.dialogo.lbl_resultado.setText('{}'.format(resultado))

        if self.dialogo.rbt_opcion5.isChecked() == True:
            mas_excusa,excusa = mod.mas_inasistencias_excusa(archivo)
            self.dialogo.lbl_resultado.setText(
                '''El congresista {}
                 falló {} veces con 
                   excusa médica'''.format(mas_excusa,excusa))

        if self.dialogo.rbt_opcion6.isChecked() == True:
            resultado = mod.asistio_fecha(archivo)
            self.dialogo.lbl_resultado.setText('{}'.format(resultado))

        if self.dialogo.rbt_opcion8.isChecked() == True:
            mes_mayor,cantidad = mod.mes_mayor_sesiones(archivo)
            self.dialogo.lbl_resultado.setText(
                '''En el mes {} 
                hubo {} sesiones'''.format(mes_mayor,cantidad))


        

if __name__ == '__main__':
    app = QApplication(sys.argv)   
    dialogo = aplicacion_congrasistas()
    dialogo.show()
    sys.exit(app.exec_())
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo adjunto
file_path = 'C:\Users\Marcia\OneDrive - uc.cl\Escritorio\grafica\presentacionfinal\yearly_combined_rio_diguillin.xlsx'
df = pd.read_excel(file_path)

# Crear la visualización
plt.figure(figsize=(10, 6))
plt.plot(df['AÑO'], df['Promedio Anual'], marker='o', linestyle='-', color='b')
plt.title('Variación del Caudal Medio Anual - Río Diguillín')
plt.xlabel('Año')
plt.ylabel('Caudal Medio Anual (m³/s)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la visualización
plt.show()


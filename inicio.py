import tkinter as tk
from tkinter import ttk, messagebox

class MatrizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones con Matrices")

        # Variables para el tamaño de la matriz y la operación (suma y resta)
        self.dimension = tk.IntVar(value=2)
        self.operacion = tk.StringVar(value="Suma")

        # Parte superior para los controles (tamaño, operación, botones)
        self.frame_config = tk.Frame(self.root)
        self.frame_config.pack(pady=10)

        # Variable que se usará para contener las matrices (se crea más adelante)
        self.matrix_frame = None

        # Crear controles y luego las matrices
        self.crear_menu_config()
        self.create_matrices()

    def crear_menu_config(self):
        """Crea los controles de configuración: tamaño, operación y botones"""
        
        tk.Label(self.frame_config, text="Tamaño de matriz:").pack(side=tk.LEFT)

        # Spinbox para elegir tamaño de la matriz (entre 1 y 5)
        tk.Spinbox(self.frame_config, from_=1, to=5, width=5, textvariable=self.dimension).pack(side=tk.LEFT, padx=5)

        # Combobox para elegir operación (suma o resta)
        tk.Label(self.frame_config, text="Operación:").pack(side=tk.LEFT)
        ttk.Combobox(
            self.frame_config,
            textvariable=self.operacion,
            values=["Suma", "Resta"],
            state="readonly",
            width=10
        ).pack(side=tk.LEFT)

        # Botón para aplicar los cambios de tamaño
        tk.Button(self.frame_config, text="Aplicar", command=self.create_matrices).pack(side=tk.LEFT, padx=5)

        # Botón para calcular la operación entre matrices
        tk.Button(self.frame_config, text="Calcular", command=self.calcular).pack(side=tk.LEFT, padx=5)

    def create_matrices(self):
        """Creates input fields for matrices A and B, and labels to display the result"""

        # If matrix frame already exists, remove it to recreate
        if self.matrix_frame:
            self.matrix_frame.destroy()

        # Main frame to hold all matrices
        self.matrix_frame = tk.Frame(self.root)
        self.matrix_frame.pack(pady=10)

        n = self.dimension.get()

        # Subframe to organize Matrix A, Matrix B, and Result side by side
        grid_frame = tk.Frame(self.matrix_frame)
        grid_frame.pack()

        # Frame for Matrix A
        frame_A = tk.Frame(grid_frame)
        frame_A.pack(side=tk.LEFT, padx=20)

        # Frame for Matrix B
        frame_B = tk.Frame(grid_frame)
        frame_B.pack(side=tk.LEFT, padx=20)

        # Frame for Result Matrix
        frame_result = tk.Frame(grid_frame)
        frame_result.pack(side=tk.LEFT, padx=20)

        # Create Matrix A
        tk.Label(frame_A, text="Matriz A").grid(row=0, column=0, columnspan=n)
        self.entries_A = [[tk.Entry(frame_A, width=5) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.entries_A[i][j].grid(row=i+1, column=j)

        # Create Matrix B
        tk.Label(frame_B, text="Matriz B").grid(row=0, column=0, columnspan=n)
        self.entries_B = [[tk.Entry(frame_B, width=5) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.entries_B[i][j].grid(row=i+1, column=j)

        # Create Result Matrix
        tk.Label(frame_result, text="Result").grid(row=0, column=0, columnspan=n)
        self.results = [[tk.Label(frame_result, text="", width=5, relief="ridge") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.results[i][j].grid(row=i+1, column=j)

    def calcular(self):
        """Toma los valores ingresados en A y B, y realiza la operación elegida"""

        try:
            n = self.dimension.get()

            # Convertir los textos de los Entry a enteros (matrices A y B)
            A = [[int(self.entries_A[i][j].get()) for j in range(n)] for i in range(n)]
            B = [[int(self.entries_B[i][j].get()) for j in range(n)] for i in range(n)]

            # Realizar la operación según lo seleccionado
            if self.operacion.get() == "Suma":
                R = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
            else:  # Resta
                R = [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

            # Mostrar los resultados en pantalla
            for i in range(n):
                for j in range(n):
                    self.results[i][j].config(text=str(R[i][j]))

        except ValueError:
            # Si algún campo no tiene número válido, mostrar error
            messagebox.showerror("Error", "Asegúrate de ingresar solo números")

# Crear ventana y ejecutar la app
root = tk.Tk()
app = MatrizApp(root)
root.mainloop()

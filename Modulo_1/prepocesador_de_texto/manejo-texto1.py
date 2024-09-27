input = """La inteligencia artificial (IA) es un campo de estudio que abarca desde la simulación del razonamiento humano hasta la creación de máquinas que pueden aprender y tomar decisiones. A lo largo de los años, la IA ha avanzado significativamente, transformando industrias como la medicina, el transporte y la educación.

El aprendizaje automático, una rama de la IA, permite que las computadoras desarrollen habilidades sin estar explícitamente programadas para ello. En lugar de seguir instrucciones específicas, las máquinas pueden analizar grandes cantidades de datos y detectar patrones para mejorar su rendimiento.

Sin embargo, con estos avances también surgen preocupaciones. La ética en la inteligencia artificial es un tema que se discute ampliamente, ya que las decisiones automatizadas pueden afectar la privacidad y los derechos de las personas. A medida que la IA continúa desarrollándose, es fundamental establecer regulaciones y principios éticos que guíen su implementación.

Por otro lado, el impacto positivo de la IA es innegable. Desde diagnósticos médicos más rápidos y precisos hasta vehículos autónomos que prometen reducir los accidentes de tránsito, las aplicaciones de la IA son diversas y están en constante expansión. En el futuro, se espera que la inteligencia artificial siga revolucionando la manera en que vivimos y trabajamos, brindando soluciones a problemas complejos que hasta hace poco parecían imposibles de resolver."""


class TextAnalyzer():
    def __init__(self, text):
        # 2. Eliminar saltos de línea y caracteres que no sean letras.
        formatted_text = text.replace(",", "").replace(
            ".", "").replace("(", "").replace(")", "")

        # 1. Convertir todo el texto a minúsculas.
        self.fmt_text = formatted_text.lower()

        # 4. Tokenizar el texto (convertirlo en una lista de palabras).
        self.word_list = self.fmt_text.split(" ")

    def freq_all(self):
        print('Texto:', self.fmt_text)
        print('Tokens:', self.word_list)

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('Texto formateado:\n')
            file.write(self.fmt_text + '\n')
            file.write('Tokens:\n')
            file.write(', '.join(self.word_list) + '\n')


# Crear instancia de TextAnalyzer
analyzerd = TextAnalyzer(input)

# Mostrar resultados en consola
analyzerd.freq_all()

# Guardar resultados en un archivo
analyzerd.save_to_file('processed-text.txt')

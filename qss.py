QSS = '''
QWidget#mainWindow {
    background-color: #2E2A24;  
    border-image: url(:/path/to/hogwarts.jpg) stretch;  
}

QWidget {
    font: 22px "Lumina";  
    color: #FFD700; 
}

QPushButton { 
    background-color: #3A3A3A;  
    border: 2px solid #8B4513; 
    color: #FFD700; 
}

QPushButton:pressed {
    background-color: #8B4513;  

QListWidget {
    background-color: #2E2A24;  
    border: 1px solid #FFD700;  
}

QListWidget::item:selected {
    background-color: #8B4513;  
}

QLabel {
    color: #FFD700;  
}

QLineEdit {
    background-color: #3A3A3A;  
    color: #FFD700;  
    border: 1px solid #8B4513;  
}

QComboBox {
    background-color: #2E2A24;  
    color: #FFD700;  
    border: 1px solid #8B4513;  
}

QComboBox QAbstractItemView {
    background-color: #3A3A3A;  
    color: #FFD700;  
}

QMenuBar {
    background-color: #2E2A24;  
}

QMenuBar::item {
    background-color: #2E2A24;  
    color: #FFD700; 
}

QMenuBar::item:selected {
    background-color: #8B4513;  
}

QMenu {
    background-color: #3A3A3A; 
    color: #FFD700;  
}

QMenu::item:selected {
    background-color: #8B4513;  
}

'''
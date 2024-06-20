import matplotlib.pyplot as plt
import numpy as np


def suite(z : np.ndarray ,c : np.ndarray) -> complex : 
    """
    Parameters
    ----------
    z : np.ndarray
        Le tableau numpy représentant les valeurs initiales.
    c : np.ndarray
        Le tableau numpy représentant les valeurs constantes c pour chaque élément de la suite.
    
    Returns
    -------
    generator
        Générateur de tableaux. Le tableau associé à la n-ème itération les n-èmes de la suite z_{n+1}=z_{n}^{2}+c, à partir des valeurs initiales présentes dans z."""
    
    while True:
        yield z
        z = z**2+c


def suite_mandelbrot(c : np.ndarray)-> np.ndarray :
    """
    Parameters
    ----------
    c : np.ndarray
        Le tableau numpy des valeurs pour générer les suites de Mandelbrot

    Returns
    -------
        generator
            Générateur de tableaux. Le tableau associé à la n-ème itération contient les n-èmes termes des suites de Mandelbrot à partir des valeurs initiales présentes dans c.
        
    """
    return suite(0,c)


def suite_julia(z : np.ndarray, c : complex ) -> np.ndarray :
    """
    Parameters
    ----------
    z : np.ndarray
        Le tableau numpy des valeurs de z_{0} pour générer les suites de Julia.

    Returns
    -------
        generator
            Générateur de tableaux. Le tableau associé à la n-ème itération contient les n-èmes termes de la suite de Julia à partir des valeurs initiales présentes dans z et du paramètre c.
        
    """
    return(suite(z,c))


def is_in_mandelbrot(c : np.ndarray, max_iter = 100) -> np.ndarray :
    """
    Parameters
    ----------
    c : np.ndarray
        Le tableau numpy pour lequel nous vérifions l'appartenance de ses éléments à l'ensemble de Mandelbrot.
    max_iter : int, optional
        Le nombre maximal d'itérations, par défaut 100.

    Returns
    -------
    np.ndarray
        Tableau de booléen : T[i][j] = True si c[i][j] dans l'ensemble de Mandelbrot après max_iter itérations, sinon False.
        

    >>> is_in_Mandelbrot(c=np.array([0.251]))
    True
    >>> is_in_Mandelbrot(c=np.array([0.251]),max_iter=100)
    False"""

    c = np.array(c)
    res = np.zeros(c.shape) 
    i = 0
    for tableau in suite_mandelbrot(c):
        i += 1
        if i < max_iter:
            res =  abs(tableau) < 2
        else :
            return(res)
        

def is_in_julia(z : np.ndarray, c : complex, max_iter = 100):
    """
    Parameters
    ----------
    z : np.ndarray
        Le tableau numpy pour lequel nous vérifions l'appartenance de ses éléments à l'ensemble de Julia.
    c : complex
        Paramètre fixé des suites de Julia
    max_iter : int, optional
        Le nombre maximal d'itérations, par défaut 100.

    Returns
    -------
    np.ndarray
        Tableau de booléen : T[i][j] = True si z[i][j] dans l'ensemble de Mandelbrot après max_iter itérations, sinon False.


    >>> is_in_Julia(z=np.array([complex(0.25,0.25)]),c=0.25)
    True
    >>> is_in_julia(z=np.array([complex(1,1)]),c=1,max_iter = 100)
    False"""
    res = np.zeros(z.shape) 
    i = 0
    for tableau in suite_julia(z,c):
        i = i+1
        if i < max_iter:
            res =  abs(tableau) < 2
        else : 
            return(res)
        

def plot_mandelbrot(zmin = complex(-2,-2), 
                    zmax = complex(2,2), 
                    pixel_size = 5e-4, 
                    max_iter = 100,
                    figname = 'mandelbrot.png'):
    """
    Parameters
    ----------
    zmin : complex, optional
        complexe correspondant au coin en bas à gauche de l'image à générer, par défaut -2-2j.
    zmax : complex, optional 
        complexe correspondant au coin en haut à droite de l'image à générer, par défaut 2+2j
    pixel_size : float, optional
        taille des pixels de l'image, par défaut 5e-4
    max_iter : int, optional
        nombre d'itérations maximum à faire dans la fonction is_in_mandelbrot, par défaut 100
    figname : string, optional
        nom à donner quand on enregistre l'image, par défaut 'mandelbrot.png'

    Returns
    -------
    None
    affiche la fractale de Mandelbrot dans le rectangle de diagonale [zmin,zmax]
    """

    largeur = int((zmax.real-zmin.real)/pixel_size)
    hauteur = int((zmax.imag-zmin.imag)/pixel_size)
    image = np.full((hauteur, largeur, 3), 255, dtype=np.uint8) #image blanche

    plt.figure(figsize = (20,20))
    plt.axis('off')

    real_part = np.linspace(zmin.real, zmax.real, largeur)
    imag_part = 1j * np.linspace(zmin.imag, zmax.imag, hauteur)
    tableau = real_part + imag_part[:, np.newaxis] # tableau des position des pixels dans le plan complexes

    tab_bool = is_in_mandelbrot(tableau, max_iter) 
    image[tab_bool] = 0  # pixels dans l'ensemble = noir 

    plt.imshow(image)
    plt.savefig(f'nos_images/{figname}')


def plot_julia(c,zmin = complex(-2,-2), 
                zmax = complex(2,2), 
                pixel_size = 5e-4, 
                max_iter = 100,
                figname = 'julia.png'):
    """
    Parameters
    ----------
    c : complex
        paramètre fixé pour toutes le suites de Julia
    zmin : complex, optional
        complexe correspondant au coin en bas à gauche de l'image à générer, par défaut -2-2j.
    zmax : complex, optional 
        complexe correspondant au coin en haut à droite de l'image à générer, par défaut 2+2j
    pixel_size : float, optional
        taille des pixels de l'image, par défaut 5e-4
    max_iter : int, optional
        nombre d'itérations maximum à faire dans la fonction is_in_julia, par défaut 100
    figname : string, optional
        nom à donner quand on enregistre l'image, par défaut 'julia.png'

    Returns
    -------
    None
    affiche la fractale de Julia dans le rectangle de diagonale [zmin,zmax]
    """

    largeur = int((zmax.real-zmin.real)/pixel_size)
    hauteur = int((zmax.imag-zmin.imag)/pixel_size)
    image = np.full((hauteur, largeur, 3), 255, dtype=np.uint8)

    plt.figure(figsize = (20,20))
    plt.axis('off')

    real_part = np.linspace(zmin.real, zmax.real, largeur)
    imag_part = 1j * np.linspace(zmin.imag, zmax.imag, hauteur)
    tableau = real_part + imag_part[:, np.newaxis]

    tab_bool = is_in_julia(tableau, c, max_iter) 
    image[tab_bool] = 0

    plt.imshow(image)
    plt.savefig(f'nosimages/{figname}')

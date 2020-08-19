from odak import np

def propagate_plane_waves(field,opd,k,w=0,t=0):
    """
    Definition to propagate a field representing a plane wave at a particular distance and time.

    Parameters
    ----------
    field        : complex
                   Complex field.
    opd          : float
                   Optical path difference in mm.
    k            : float
                   Wave number of a wave, see odak.wave.parameters.wavenumber for more.
    w            : float
                   Rotation speed of a wave, see odak.wave.parameters.rotationspeed for more.
    t            : float
                   Time in seconds.

    Returns
    ----------
    new_field     : complex
                    A complex number that provides the resultant field in the complex form A*e^(j(wt+phi)).
    """
    new_field = field*np.exp(1j*(-w*t+opd*k))
    return new_field

def electric_field_per_plane_wave(amplitude,opd,k,phase=0,w=0,t=0):
    """
    Definition to return state of a plane wave at a particular distance and time.

    Parameters
    ----------
    amplitude    : float
                   Amplitude of a wave.
    opd          : float
                   Optical path difference in mm.
    k            : float
                   Wave number of a wave, see odak.wave.parameters.wavenumber for more.
    phase        : float
                   Initial phase of a wave.
    w            : float
                   Rotation speed of a wave, see odak.wave.parameters.rotationspeed for more.
    t            : float
                   Time in seconds.

    Returns
    ----------
    field        : complex
                   A complex number that provides the resultant field in the complex form A*e^(j(wt+phi)).
    """
    field = amplitude*np.exp(1j*(-w*t+opd*k+phase))/opd**2
    return field

def calculate_phase(field,deg=False):
    """
    Definition to calculate phase of a single or multiple given electric field(s).

    Parameters
    ----------
    field        : ndarray.complex or complex
                   Electric fields or an electric field.
    deg          : bool
                   If set True, the angles will be returned in degrees.

    Returns
    ----------
    phase        : float
                   Phase or phases of electric field(s) in radians.
    """
    phase = np.angle(field,deg=deg)
    return phase

def calculate_amplitude(field):
    """
    Definition to calculate amplitude of a single or multiple given electric field(s).

    Parameters
    ----------
    field        : ndarray.complex or complex
                   Electric fields or an electric field.

    Returns
    ----------
    amplitude    : float
                   Amplitude or amplitudes of electric field(s).
    """
    amplitude = np.abs(field)
    return amplitude

def calculate_intensity(field):
    """
    Definition to calculate intensity of a single or multiple given electric field(s).

    Parameters
    ----------
    field        : ndarray.complex or complex
                   Electric fields or an electric field.

    Returns
    ----------
    intensity    : float
                   Intensity or intensities of electric field(s).
    """
    intensity = np.abs(field)**2
    return intensity

def wavenumber(wavelength):
    """
    Definition for calculating the wavenumber of a plane wave.

    Parameters
    ----------
    wavelength   : float
                   Wavelength of a wave in mm.

    Returns
    ----------
    k            : float
                   Wave number for a given wavelength.
    """
    k = 2*np.pi/wavelength
    return k

def rotationspeed(wavelength,c=3*10**11):
    """
    Definition for calculating rotation speed of a wave (w in A*e^(j(wt+phi))).

    Parameters
    ----------
    wavelength   : float
                   Wavelength of a wave in mm.
    c            : float
                   Speed of wave in mm/seconds. Default is the speed of light in the void!

    Returns
    ----------
    w            : float

    """
    f = c*wavelength
    w = 2*np.pi*f
    return w


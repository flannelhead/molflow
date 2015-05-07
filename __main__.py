import argparse
from .molecularflow import runSimulation

parser = argparse.ArgumentParser(
    prog='python -m molecularflow',
    description='Compute molecular flow particle densities in an elbow tube',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('A', type=float, help='Tube dimension A [m]')
parser.add_argument('B', type=float, help='Tube dimension B [m]')
parser.add_argument('filename', help='Filename (.npz) to save the results to')
parser.add_argument('-N', type=int, help='Number of test particles',
                    default=10000)
parser.add_argument('-Q', type=float, help='Flow rate [Pa m^3]', default=0.01)
parser.add_argument('-Z', type=float, help='Mass of the molecules [amu]',
                    default=28)
parser.add_argument('-T', type=float, help='Temperature of the system [K]',
                    default=300)
parser.add_argument('--grid-size', type=float, help='Grid size [m]',
                    default=0.2)
parser.add_argument('--dt', type=float, help='Grid size [m]',
                    default=1e-3)
parser.add_argument('--sample-mb', dest='sambleMB',
                    action='store_true',
                    default=False, help='Sample speeds from the MB '
                    'distribution instead of using the mean')

args = parser.parse_args()
runSimulation(args.A, args.B, Q=args.Q, Z=args.Z, T=args.T, N=args.N,
              dx=args.grid_size, dt=args.dt, filename=args.filename)
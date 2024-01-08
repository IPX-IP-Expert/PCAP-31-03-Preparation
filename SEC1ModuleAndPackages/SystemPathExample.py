import sys

# Print the system path
print(sys.path)

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(
    "/home/deivy/Desktop/Study/PCAP-31-03-Preparation/SEC1ModuleAndPackages/Modules/"
)


print(f"\n...appending to system path sys.path = {sys.path} ")

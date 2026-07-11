import os
from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def plot_radar_layers_high_contrast():
    
    data_dir = Path('./data/raw/coverage')
    
    if not os.path.exists(data_dir):
        print(f"Error: Directory '{data_dir}' not found. Please run the download script first.")
        return
        
    shp_files = [f for f in os.listdir(data_dir) if f.endswith('.shp')]
    if not shp_files:
        print("Error: No .shp file found in the directory.")
        return
        
    shp_path = os.path.join(data_dir, shp_files[0])
    
    gdf = gpd.read_file(shp_path)
    
    gdf['height'] = gdf['height'].astype(int)
    
    gdf_10k = gdf[gdf['height'] == 10000]
    gdf_6k  = gdf[gdf['height'] == 6000]
    gdf_3k  = gdf[gdf['height'] == 3000]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    ax.set_xlim([-130, -64])
    ax.set_ylim([20, 52])
    
    print("Plotting 10,000 ft AGL layer (Deep Gold)...")
    gdf_10k.plot(ax=ax, color='#fbc02d', alpha=0.4, edgecolor='#f57f17', linewidth=0.5)
    
    print("Plotting 6,000 ft AGL layer (Orange)...")
    gdf_6k.plot(ax=ax, color='#ff9800', alpha=0.55, edgecolor='#e65100', linewidth=0.5)
    
    print("Plotting 3,000 ft AGL layer (Red)...")
    gdf_3k.plot(ax=ax, color='#f44336', alpha=0.65, edgecolor='#b71c1c', linewidth=0.5)
    
    ax.set_title("NEXRAD Complex Radar Coverage Layers: April 30, 2026", color='black', fontsize=16, pad=15, weight='bold') # (Terrain Masked)
    ax.set_xlabel("Longitude" + r'[$\degree$]', color='black', fontsize=16, weight='bold')
    ax.set_ylabel("Latitude" + r'[$\degree$]', color='black', fontsize=16, weight='bold')
    
    ax.tick_params(colors='black', which='both', labelsize=10)
    
    ax.grid(True, linestyle='--', alpha=0.2, color='#757575')
    
    legend_elements = [
        Patch(facecolor='#fbc02d', alpha=0.5, edgecolor='#f57f17', label='10,000 ft AGL Coverage'),
        Patch(facecolor='#ff9800', alpha=0.6, edgecolor='#e65100', label='6,000 ft AGL Coverage'),
        Patch(facecolor='#f44336', alpha=0.7, edgecolor='#b71c1c', label='3,000 ft AGL Coverage')
    ]
    ax.legend(handles=legend_elements, loc='lower left', facecolor='#ffffff', edgecolor='black', labelcolor='black')
    
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1.2)
        
    plt.tight_layout()
    
    output_png = Path("plots/NEXRAD_AGL_Layers_High_Contrast.png")
    plt.savefig(output_png, dpi=300, facecolor='white', edgecolor='none')
    print(f"Map successfully saved to disk as: {output_png}")
    plt.show()

if __name__ == "__main__":
    plot_radar_layers_high_contrast()
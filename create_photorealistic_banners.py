"""
Create photorealistic AI-inspired banner images for GitHub projects.
Style: Medical/scientific imaging with glowing effects, neural networks, and 3D visualization.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

def create_gradient_with_glow(width, height, base_color, glow_positions):
    """Create background with glowing effect."""
    image = Image.new('RGB', (width, height), base_color)
    
    # Add glow effects
    for x, y, radius, color in glow_positions:
        glow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(glow)
        
        # Create multiple layers for glow effect
        for i in range(20):
            alpha = int(100 * (1 - i/20))
            r_curr = radius + i * 15
            draw.ellipse([x-r_curr, y-r_curr, x+r_curr, y+r_curr], 
                        fill=color + (alpha,))
        
        image = Image.alpha_composite(image.convert('RGBA'), glow).convert('RGB')
    
    return image

def draw_neural_network(draw, start_x, start_y, width, height, color):
    """Draw a neural network visualization."""
    layers = [4, 6, 6, 4]  # nodes per layer
    layer_spacing = width // (len(layers) + 1)
    
    nodes = []
    # Calculate node positions
    for layer_idx, num_nodes in enumerate(layers):
        x = start_x + layer_spacing * (layer_idx + 1)
        layer_nodes = []
        for node_idx in range(num_nodes):
            y = start_y + height // 2 - (num_nodes - 1) * 20 + node_idx * 40
            layer_nodes.append((x, y))
        nodes.append(layer_nodes)
    
    # Draw connections
    for i in range(len(nodes) - 1):
        for node1 in nodes[i]:
            for node2 in nodes[i + 1]:
                draw.line([node1, node2], fill=color + (60,), width=1)
    
    # Draw nodes
    for layer in nodes:
        for node in layer:
            draw.ellipse([node[0]-8, node[1]-8, node[0]+8, node[1]+8], 
                        fill=color + (200,), outline=color + (255,), width=2)

def draw_dna_helix(draw, start_x, start_y, height, color):
    """Draw a DNA helix structure."""
    turns = 3
    points_per_turn = 30
    total_points = turns * points_per_turn
    
    helix1_points = []
    helix2_points = []
    
    for i in range(total_points):
        t = i / points_per_turn * 2 * math.pi
        y = start_y + (i / total_points) * height
        
        x1 = start_x + math.sin(t) * 30
        x2 = start_x - math.sin(t) * 30
        
        helix1_points.append((x1, y))
        helix2_points.append((x2, y))
        
        # Draw connecting bars every quarter turn
        if i % (points_per_turn // 4) == 0:
            draw.line([(x1, y), (x2, y)], fill=color + (150,), width=2)
    
    # Draw helices
    for i in range(len(helix1_points) - 1):
        draw.line([helix1_points[i], helix1_points[i+1]], fill=color + (255,), width=3)
        draw.line([helix2_points[i], helix2_points[i+1]], fill=color + (255,), width=3)

def draw_molecular_structure(draw, center_x, center_y, radius, color):
    """Draw a molecular structure with nodes and bonds."""
    # Central node
    draw.ellipse([center_x-15, center_y-15, center_x+15, center_y+15],
                fill=color + (255,), outline=color + (255,), width=3)
    
    # Surrounding nodes
    num_nodes = 6
    for i in range(num_nodes):
        angle = i * (360 / num_nodes) * (math.pi / 180)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # Draw bond
        draw.line([(center_x, center_y), (x, y)], fill=color + (200,), width=3)
        
        # Draw node
        draw.ellipse([x-10, y-10, x+10, y+10],
                    fill=color + (220,), outline=color + (255,), width=2)

def draw_grid_overlay(draw, width, height, color):
    """Draw a futuristic grid overlay."""
    spacing = 50
    for x in range(0, width, spacing):
        draw.line([(x, 0), (x, height)], fill=color + (20,), width=1)
    for y in range(0, height, spacing):
        draw.line([(0, y), (width, y)], fill=color + (20,), width=1)

def create_biomap_banner():
    """Create photorealistic banner for BioMap project."""
    width, height = 1200, 400
    
    # Dark blue-teal base
    base_color = (10, 20, 40)
    
    # Add glowing areas (x, y, radius, color)
    glows = [
        (200, 200, 100, (0, 150, 200)),  # Cyan glow
        (800, 150, 120, (100, 50, 200)),  # Purple glow
        (1000, 300, 80, (0, 200, 150)),   # Teal glow
    ]
    
    image = create_gradient_with_glow(width, height, base_color, glows)
    
    # Create overlay for graphics
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Draw grid
    draw_grid_overlay(draw, width, height, (100, 200, 255))
    
    # Draw neural network
    draw_neural_network(draw, 650, 100, 350, 200, (0, 200, 255))
    
    # Draw DNA helix
    draw_dna_helix(draw, 550, 80, 280, (0, 255, 200))
    
    # Add some glowing particles
    for _ in range(30):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(1, 3)
        alpha = random.randint(100, 200)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(100, 200, 255, alpha))
    
    # Combine
    image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add text
    draw = ImageDraw.Draw(image)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 72)
        subtitle_font = ImageFont.truetype("arial.ttf", 32)
        desc_font = ImageFont.truetype("arial.ttf", 22)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    # Add title with glow
    title = "BioMap"
    subtitle = "Biomedical Entity Linking"
    desc = "AI-Powered Biomedical NLP"
    
    # Shadow/glow
    for offset in [(2, 2), (1, 1), (0, 0)]:
        alpha = 255 if offset == (0, 0) else 100
        draw.text((50 + offset[0], 80 + offset[1]), title, 
                 font=title_font, fill=(100, 220, 255, alpha))
    
    draw.text((50, 170), subtitle, font=subtitle_font, fill=(180, 230, 255))
    draw.text((50, 220), desc, font=desc_font, fill=(150, 200, 255))
    
    # Add badge indicators
    badge_y = 300
    draw.rectangle([45, badge_y, 160, badge_y + 35], 
                  outline=(0, 200, 255), width=2)
    draw.text((55, badge_y + 5), "SapBERT", font=desc_font, fill=(200, 240, 255))
    
    draw.rectangle([175, badge_y, 320, badge_y + 35], 
                  outline=(100, 150, 255), width=2)
    draw.text((185, badge_y + 5), "BioMegatron", font=desc_font, fill=(200, 240, 255))
    
    return image

def create_diffbind_banner():
    """Create photorealistic banner for DiffBind project."""
    width, height = 1200, 400
    
    # Dark purple-pink base
    base_color = (25, 10, 35)
    
    # Add glowing areas
    glows = [
        (300, 200, 150, (150, 50, 150)),  # Purple glow
        (900, 200, 120, (200, 50, 100)),  # Pink glow
        (600, 100, 80, (100, 100, 200)),  # Blue glow
    ]
    
    image = create_gradient_with_glow(width, height, base_color, glows)
    
    # Create overlay
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Draw grid
    draw_grid_overlay(draw, width, height, (200, 100, 200))
    
    # Draw molecular structures
    draw_molecular_structure(draw, 750, 150, 80, (255, 100, 200))
    draw_molecular_structure(draw, 900, 250, 60, (200, 150, 255))
    
    # Draw protein structure (simplified)
    for i in range(5):
        x = 600 + i * 40
        y = 200 + math.sin(i) * 30
        draw.ellipse([x-12, y-12, x+12, y+12], 
                    fill=(200, 100, 255, 200), outline=(255, 150, 255, 255), width=2)
        if i > 0:
            prev_x = 600 + (i-1) * 40
            prev_y = 200 + math.sin(i-1) * 30
            draw.line([(prev_x, prev_y), (x, y)], fill=(255, 150, 255, 180), width=3)
    
    # Add glowing particles
    for _ in range(40):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(1, 4)
        alpha = random.randint(80, 180)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(255, 100, 200, alpha))
    
    # Combine
    image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add text
    draw = ImageDraw.Draw(image)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 72)
        subtitle_font = ImageFont.truetype("arial.ttf", 32)
        desc_font = ImageFont.truetype("arial.ttf", 22)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    title = "DiffBind"
    subtitle = "Diffusion Models for Drug Discovery"
    desc = "Protein-Ligand Binding Prediction"
    
    # Glow effect
    for offset in [(2, 2), (1, 1), (0, 0)]:
        alpha = 255 if offset == (0, 0) else 100
        draw.text((50 + offset[0], 80 + offset[1]), title, 
                 font=title_font, fill=(255, 150, 220, alpha))
    
    draw.text((50, 170), subtitle, font=subtitle_font, fill=(255, 180, 230))
    draw.text((50, 220), desc, font=desc_font, fill=(255, 150, 200))
    
    # Add badges
    badge_y = 300
    draw.rectangle([45, badge_y, 130, badge_y + 35], 
                  outline=(255, 100, 200), width=2)
    draw.text((55, badge_y + 5), "DDPM", font=desc_font, fill=(255, 200, 230))
    
    draw.rectangle([145, badge_y, 320, badge_y + 35], 
                  outline=(200, 100, 255), width=2)
    draw.text((155, badge_y + 5), "Equivariant NNs", font=desc_font, fill=(255, 200, 230))
    
    return image

def create_catflix_banner():
    """Create photorealistic banner for Catflix project."""
    width, height = 1200, 400
    
    # Dark cyan-blue base
    base_color = (5, 15, 30)
    
    # Add glowing areas
    glows = [
        (200, 200, 140, (0, 180, 220)),   # Bright cyan
        (900, 150, 100, (0, 220, 255)),   # Light blue
        (600, 280, 90, (100, 200, 255)),  # Sky blue
    ]
    
    image = create_gradient_with_glow(width, height, base_color, glows)
    
    # Create overlay
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Draw grid
    draw_grid_overlay(draw, width, height, (0, 200, 255))
    
    # Draw playful elements (motion trails, particles)
    for i in range(10):
        x = 600 + i * 50
        y = 150 + math.sin(i * 0.5) * 80
        size = 15 - i
        alpha = 200 - i * 15
        draw.ellipse([x-size, y-size, x+size, y+size], 
                    fill=(0, 255, 255, alpha))
    
    # Draw animated path
    path_points = []
    for i in range(20):
        t = i / 10
        x = 550 + i * 30
        y = 200 + math.sin(t * math.pi) * 60
        path_points.append((x, y))
    
    for i in range(len(path_points) - 1):
        alpha = 100 + i * 7
        draw.line([path_points[i], path_points[i+1]], 
                 fill=(0, 255, 255, alpha), width=4)
    
    # Add sparkle effects
    for _ in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(1, 3)
        alpha = random.randint(100, 255)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(100, 230, 255, alpha))
        # Add small cross for sparkle
        if random.random() > 0.7:
            draw.line([(x-5, y), (x+5, y)], fill=(200, 255, 255, alpha), width=1)
            draw.line([(x, y-5), (x, y+5)], fill=(200, 255, 255, alpha), width=1)
    
    # Combine
    image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    # Add text
    draw = ImageDraw.Draw(image)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 72)
        subtitle_font = ImageFont.truetype("arial.ttf", 32)
        desc_font = ImageFont.truetype("arial.ttf", 22)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    title = "Catflix"
    subtitle = "AI-Generated Cat Entertainment"
    desc = "Procedural Animation & Automation"
    
    # Glow effect
    for offset in [(2, 2), (1, 1), (0, 0)]:
        alpha = 255 if offset == (0, 0) else 100
        draw.text((50 + offset[0], 80 + offset[1]), title, 
                 font=title_font, fill=(100, 240, 255, alpha))
    
    draw.text((50, 170), subtitle, font=subtitle_font, fill=(150, 240, 255))
    draw.text((50, 220), desc, font=desc_font, fill=(120, 220, 255))
    
    # Add badges
    badge_y = 300
    draw.rectangle([45, badge_y, 160, badge_y + 35], 
                  outline=(0, 220, 255), width=2)
    draw.text((55, badge_y + 5), "MoviePy", font=desc_font, fill=(200, 250, 255))
    
    draw.rectangle([175, badge_y, 280, badge_y + 35], 
                  outline=(100, 200, 255), width=2)
    draw.text((185, badge_y + 5), "YouTube", font=desc_font, fill=(200, 250, 255))
    
    return image

if __name__ == "__main__":
    print("Creating photorealistic AI-inspired banners...")
    
    # Create banners
    biomap_banner = create_biomap_banner()
    diffbind_banner = create_diffbind_banner()
    catflix_banner = create_catflix_banner()
    
    # Save banners
    biomap_banner.save("biomap_banner_v2.png", quality=95)
    diffbind_banner.save("diffbind_banner_v2.png", quality=95)
    catflix_banner.save("catflix_banner_v2.png", quality=95)
    
    print("[OK] biomap_banner_v2.png created")
    print("[OK] diffbind_banner_v2.png created")
    print("[OK] catflix_banner_v2.png created")
    print("\nPhotorealistic banners created successfully!")

"""Set 2 of the Cali IT logo options (51-100): different styles drawn from how IT and consulting firms present themselves.
Ideas used: restrained wordmarks, custom lettermarks, step shapes for progress, a slash or prompt for computing, connected nodes,
intersecting shapes, layered infrastructure, a small 3D cube, seals and badges, and refined serif type with one accent color."""

# Each mark draws inside a 64x64 box.  c1 = main color, c2 = accent, k = color for cut-outs (white on light, page color on dark).
def step_c(c1, c2, k): return f'<path d="M50 10 H22 V18 H14 V46 H22 V54 H50 V44 H26 V20 H50Z" fill="{c1}"/><rect x="40" y="27" width="10" height="10" fill="{c2}"/>'
def interlock(c1, c2, k): return f'<circle cx="24" cy="32" r="16" fill="none" stroke="{c1}" stroke-width="6"/><circle cx="40" cy="32" r="16" fill="none" stroke="{c2}" stroke-width="6"/><path d="M32 18.2 A16 16 0 0 1 32 45.8" fill="none" stroke="{c1}" stroke-width="6"/>'
def orbit(c1, c2, k): return f'<circle cx="32" cy="32" r="13" fill="{c1}"/><ellipse cx="32" cy="32" rx="28" ry="11" fill="none" stroke="{c1}" stroke-width="3" transform="rotate(-25 32 32)"/><circle cx="56" cy="21" r="5" fill="{c2}"/>'
def chip(c1, c2, k):
    pins = ''.join(f'<rect x="{x}" y="4" width="4" height="8" rx="1" fill="{c1}"/><rect x="{x}" y="52" width="4" height="8" rx="1" fill="{c1}"/><rect x="4" y="{x}" width="8" height="4" rx="1" fill="{c1}"/><rect x="52" y="{x}" width="8" height="4" rx="1" fill="{c1}"/>' for x in (20, 30, 40))
    return pins + f'<rect x="12" y="12" width="40" height="40" rx="6" fill="{c1}"/><path d="M39 24 A10 10 0 1 0 39 40" fill="none" stroke="{k}" stroke-width="5" stroke-linecap="round"/><circle cx="42" cy="32" r="3" fill="{c2}"/>'
def arrow_c(c1, c2, k): return f'<path d="M46 46 A20 20 0 1 1 46 18" fill="none" stroke="{c1}" stroke-width="8" stroke-linecap="round"/><path d="M36 10 H50 V24" fill="none" stroke="{c2}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
def ridge(c1, c2, k): return f'<circle cx="32" cy="32" r="28" fill="{c1}"/><path d="M8 44 L22 28 L30 36 L40 22 L56 42 A28 28 0 0 1 8 44Z" fill="{k}"/><circle cx="44" cy="17" r="4" fill="{c2}"/>'
def squares(c1, c2, k): return f'<rect x="6" y="6" width="52" height="52" rx="4" fill="none" stroke="{c1}" stroke-width="4"/><rect x="16" y="16" width="32" height="32" rx="3" fill="none" stroke="{c1}" stroke-width="4"/><rect x="26" y="26" width="12" height="12" rx="2" fill="{c2}"/>'
def cube(c1, c2, k): return f'<path d="M32 6 L56 19 L32 32 L8 19Z" fill="{c2}"/><path d="M8 19 L32 32 V58 L8 45Z" fill="{c1}"/><path d="M56 19 L32 32 V58 L56 45Z" fill="{c1}" opacity=".72"/>'
def cube_line(c1, c2, k): return f'<path d="M32 6 L56 19 V45 L32 58 L8 45 V19Z M8 19 L32 32 L56 19 M32 32 V58" fill="none" stroke="{c1}" stroke-width="4" stroke-linejoin="round"/><path d="M32 6 L56 19 L32 32 L8 19Z" fill="{c2}"/>'
def layers(c1, c2, k): return f'<path d="M32 8 L58 20 L32 32 L6 20Z" fill="{c2}"/><path d="M6 31 L32 43 L58 31" fill="none" stroke="{c1}" stroke-width="5" stroke-linejoin="round"/><path d="M6 42 L32 54 L58 42" fill="none" stroke="{c1}" stroke-width="5" stroke-linejoin="round"/>'
def pixel_c(c1, c2, k):
    rows = ['01110', '10000', '10000', '10001', '01110']
    out = ''
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            if v == '1':
                out += f'<rect x="{7 + c * 10.5}" y="{7 + r * 10.5}" width="9" height="9" rx="1.5" fill="{c2 if (r, c) == (3, 4) else c1}"/>'
    return out
def arch(c1, c2, k): return f'<path d="M6 54 V36 A26 26 0 0 1 58 36 V54" fill="none" stroke="{c1}" stroke-width="6"/><path d="M16 54 V38 A16 16 0 0 1 48 38 V54" fill="none" stroke="{c1}" stroke-width="4"/><rect x="4" y="52" width="56" height="5" rx="2" fill="{c2}"/>'
def keyhole(c1, c2, k): return f'<circle cx="32" cy="32" r="28" fill="{c1}"/><circle cx="32" cy="26" r="8" fill="{k}"/><path d="M27 30 L24 46 H40 L37 30Z" fill="{k}"/><circle cx="32" cy="26" r="3" fill="{c2}"/>'
def shield_check(c1, c2, k): return f'<path d="M32 5 L55 13 V30 C55 45 45 55 32 59 C19 55 9 45 9 30 V13Z" fill="none" stroke="{c1}" stroke-width="5" stroke-linejoin="round"/><path d="M21 32 L29 40 L44 24" fill="none" stroke="{c2}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
def compass(c1, c2, k): return f'<circle cx="32" cy="32" r="27" fill="none" stroke="{c1}" stroke-width="4"/><path d="M32 9 L37 32 L32 55 L27 32Z" fill="{c1}"/><path d="M9 32 L32 27 L55 32 L32 37Z" fill="{c1}" opacity=".45"/><path d="M32 9 L37 32 L27 32Z" fill="{c2}"/>'
def sunrays(c1, c2, k):
    import math
    rays = ''.join(f'<line x1="{32 + 20 * math.cos(math.radians(a)):.1f}" y1="{44 - 20 * math.sin(math.radians(a)):.1f}" x2="{32 + 28 * math.cos(math.radians(a)):.1f}" y2="{44 - 28 * math.sin(math.radians(a)):.1f}" stroke="{c1}" stroke-width="4" stroke-linecap="round"/>' for a in range(15, 180, 30))
    return rays + f'<path d="M18 44 A14 14 0 0 1 46 44Z" fill="{c2}"/><rect x="6" y="48" width="52" height="5" rx="2.5" fill="{c1}"/>'
def graph(c1, c2, k):
    pts = [(12, 44), (24, 16), (42, 24), (52, 48), (32, 40)]
    lines = ''.join(f'<line x1="{pts[a][0]}" y1="{pts[a][1]}" x2="{pts[b][0]}" y2="{pts[b][1]}" stroke="{c1}" stroke-width="3"/>' for a, b in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (2, 4)])
    dots = ''.join(f'<circle cx="{x}" cy="{y}" r="{7 if i == 4 else 5}" fill="{c2 if i == 4 else c1}"/>' for i, (x, y) in enumerate(pts))
    return lines + dots
def infinity(c1, c2, k): return f'<path d="M32 32 C24 20 8 20 8 32 C8 44 24 44 32 32" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round"/><path d="M32 32 C40 20 56 20 56 32 C56 44 40 44 32 32" fill="none" stroke="{c2}" stroke-width="6" stroke-linecap="round"/>'
def diamond_i(c1, c2, k): return f'<path d="M32 4 L60 32 L32 60 L4 32Z" fill="{c1}"/><rect x="29" y="27" width="6" height="18" rx="1" fill="{k}"/><circle cx="32" cy="20" r="4" fill="{c2}"/>'
def quads(c1, c2, k): return f'<path d="M30 30 V6 A24 24 0 0 0 6 30Z" fill="{c1}"/><path d="M30 34 H6 A24 24 0 0 0 30 58Z" fill="{c1}"/><path d="M34 34 V58 A24 24 0 0 0 58 34Z" fill="{c1}" opacity=".35"/><path d="M34 30 H58 A24 24 0 0 0 34 6Z" fill="{c2}"/>'
def ci_lig(c1, c2, k, f='inherit'): return f'<circle cx="32" cy="32" r="28" fill="none" stroke="{c1}" stroke-width="3"/><text x="31" y="42" text-anchor="middle" font-family="{f}" font-weight="700" font-size="28" fill="{c1}">ci</text><circle cx="40.5" cy="17.5" r="3.4" fill="{c2}"/>'
def code_br(c1, c2, k): return f'<path d="M20 14 L6 32 L20 50" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 14 L58 32 L44 50" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M36 12 L28 52" stroke="{c2}" stroke-width="6" stroke-linecap="round"/>'
def gradient_ring(c1, c2, k, gid='g'): return f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs><path d="M47 15 A24 24 0 1 0 47 49" fill="none" stroke="url(#{gid})" stroke-width="10" stroke-linecap="round"/>'
def molecule(c1, c2, k): return f'<path d="M32 8 L53 20 V44 L32 56 L11 44 V20Z" fill="none" stroke="{c1}" stroke-width="3.5"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c1}"/>' for x, y in [(32, 8), (53, 20), (53, 44), (32, 56), (11, 44), (11, 20)]) + f'<circle cx="32" cy="32" r="7" fill="{c2}"/>'
def cloud_up(c1, c2, k): return f'<path d="M18 48 A11 11 0 0 1 17 26 A15 15 0 0 1 45 22 A12 12 0 0 1 47 48Z" fill="none" stroke="{c1}" stroke-width="4.5" stroke-linejoin="round"/><path d="M32 44 V28 M25 34 L32 27 L39 34" fill="none" stroke="{c2}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
def lock_line(c1, c2, k): return f'<path d="M22 28 V20 A10 10 0 0 1 42 20 V24" fill="none" stroke="{c1}" stroke-width="5" stroke-linecap="round"/><rect x="12" y="28" width="40" height="30" rx="7" fill="none" stroke="{c1}" stroke-width="5"/><circle cx="32" cy="42" r="4.5" fill="{c2}"/>'
def wave_sq(c1, c2, k): return f'<rect x="6" y="6" width="52" height="52" rx="10" fill="{c1}"/><path d="M6 38 Q19 28 32 38 T58 38 V48 A10 10 0 0 1 48 58 H16 A10 10 0 0 1 6 48Z" fill="{c2}"/><circle cx="42" cy="22" r="6" fill="{k}"/>'
def peaks_up(c1, c2, k): return f'<path d="M6 54 L22 30 L32 42 L46 18 L58 36" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 14 H50 V24" fill="none" stroke="{c2}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
def frame_c(c1, c2, k): return f'<path d="M6 18 V6 H18 M46 6 H58 V18 M58 46 V58 H46 M18 58 H6 V46" fill="none" stroke="{c1}" stroke-width="4"/><path d="M42 22 A12 12 0 1 0 42 42" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round"/><circle cx="44" cy="32" r="3.5" fill="{c2}"/>'
def signal_i(c1, c2, k): return f'<rect x="27" y="34" width="10" height="24" rx="3" fill="{c1}"/><circle cx="32" cy="24" r="5" fill="{c2}"/><path d="M20 16 A16 16 0 0 1 44 16" fill="none" stroke="{c1}" stroke-width="4" stroke-linecap="round"/><path d="M12 8 A26 26 0 0 1 52 8" fill="none" stroke="{c1}" stroke-width="4" stroke-linecap="round" opacity=".55"/>'
def half_disc(c1, c2, k): return f'<path d="M32 6 A26 26 0 0 0 32 58Z" fill="{c1}"/><path d="M36 6 A26 26 0 0 1 36 58Z" fill="{c2}"/>'

MARKS2 = [('Step C', step_c), ('Linked rings', interlock), ('Orbit', orbit), ('Chip', chip), ('Arrow C', arrow_c), ('Sierra', ridge),
          ('Nested squares', squares), ('Cube', cube), ('Line cube', cube_line), ('Stack', layers), ('Pixel C', pixel_c), ('Arch', arch),
          ('Keyhole', keyhole), ('Shield check', shield_check), ('Compass', compass), ('Sunrise', sunrays), ('Network graph', graph),
          ('Infinity', infinity), ('Diamond i', diamond_i), ('Quarters', quads), ('ci monogram', ci_lig), ('Code slash', code_br),
          ('Gradient C', gradient_ring), ('Hex network', molecule), ('Cloud upload', cloud_up), ('Line lock', lock_line),
          ('Wave tile', wave_sq), ('Growth line', peaks_up), ('Focus C', frame_c), ('Signal i', signal_i), ('Halves', half_disc)]

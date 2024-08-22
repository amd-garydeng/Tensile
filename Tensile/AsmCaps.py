################################################################################
#
# Copyright (C) 2023-2024 Advanced Micro Devices, Inc. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
################################################################################

CACHED_ASM_CAPS = \
{(0, 0, 0): {'HasAddLshl': False,
             'HasAtomicAdd': False,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': False,
             'HasExplicitCO': False,
             'HasExplicitNC': False,
             'HasGLCModifier': False,
             'HasNTModifier': False,
             'HasLshlOr': False,
             'HasMFMA': False,
             'HasMFMA_b8': False,
             'HasMFMA_bf16_1k': False,
             'HasMFMA_bf16_original': False,
             'HasMFMA_constSrc': False,
             'HasMFMA_f64': False,
             'HasMFMA_f8': False,
             'HasMFMA_i8_908': False,
             'HasMFMA_i8_940': False,
             'HasMFMA_vgpr': False,
             'HasMFMA_xf32': False,
             'HasSMulHi': False,
             'HasWMMA': False,
             'KernargPreloading': False,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 0,
             'SupportedISA': False,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': False,
             'v_dot2_f32_f16': False,
             'v_dot2c_f32_f16': False,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': False,
             'v_fma_f16': False,
             'v_fma_f32': False,
             'v_fma_f64': False,
             'v_fma_mix_f32': False,
             'v_fmac_f16': False,
             'v_fmac_f32': False,
             'v_mac_f16': False,
             'v_mac_f32': False,
             'v_mad_mix_f32': False,
             'v_mov_b64': False,
             'v_pk_fma_f16': False,
             'v_pk_fmac_f16': False},
 (8, 0, 3): {'HasAddLshl': False,
             'HasAtomicAdd': False,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': True,
             'HasExplicitCO': False,
             'HasExplicitNC': False,
             'HasGLCModifier': True,
             'HasNTModifier': False,
             'HasLshlOr': False,
             'HasMFMA': False,
             'HasMFMA_b8': False,
             'HasMFMA_bf16_1k': False,
             'HasMFMA_bf16_original': False,
             'HasMFMA_constSrc': False,
             'HasMFMA_f64': False,
             'HasMFMA_f8': False,
             'HasMFMA_i8_908': False,
             'HasMFMA_i8_940': False,
             'HasMFMA_vgpr': False,
             'HasMFMA_xf32': False,
             'HasSMulHi': False,
             'HasWMMA': False,
             'KernargPreloading': False,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 15,
             'SupportedISA': True,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': False,
             'v_dot2_f32_f16': False,
             'v_dot2c_f32_f16': False,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': False,
             'v_fma_f16': False,
             'v_fma_f32': True,
             'v_fma_f64': True,
             'v_fma_mix_f32': False,
             'v_fmac_f16': False,
             'v_fmac_f32': False,
             'v_mac_f16': True,
             'v_mac_f32': True,
             'v_mad_mix_f32': False,
             'v_mov_b64': False,
             'v_pk_fma_f16': False,
             'v_pk_fmac_f16': False},
 (9, 0, 0): {'HasAddLshl': True,
             'HasAtomicAdd': False,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': True,
             'HasExplicitCO': True,
             'HasExplicitNC': False,
             'HasGLCModifier': True,
             'HasNTModifier': False,
             'HasLshlOr': True,
             'HasMFMA': False,
             'HasMFMA_b8': False,
             'HasMFMA_bf16_1k': False,
             'HasMFMA_bf16_original': False,
             'HasMFMA_constSrc': False,
             'HasMFMA_f64': False,
             'HasMFMA_f8': False,
             'HasMFMA_i8_908': False,
             'HasMFMA_i8_940': False,
             'HasMFMA_vgpr': False,
             'HasMFMA_xf32': False,
             'HasSMulHi': True,
             'HasWMMA': False,
             'KernargPreloading': False,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 63,
             'SupportedISA': True,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': False,
             'v_dot2_f32_f16': False,
             'v_dot2c_f32_f16': False,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': False,
             'v_fma_f16': True,
             'v_fma_f32': True,
             'v_fma_f64': True,
             'v_fma_mix_f32': False,
             'v_fmac_f16': False,
             'v_fmac_f32': False,
             'v_mac_f16': True,
             'v_mac_f32': True,
             'v_mad_mix_f32': True,
             'v_mov_b64': False,
             'v_pk_fma_f16': True,
             'v_pk_fmac_f16': False},
 (9, 0, 6): {'HasAddLshl': True,
             'HasAtomicAdd': False,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': True,
             'HasExplicitCO': True,
             'HasExplicitNC': False,
             'HasGLCModifier': True,
             'HasNTModifier': False,
             'HasLshlOr': True,
             'HasMFMA': False,
             'HasMFMA_b8': False,
             'HasMFMA_bf16_1k': False,
             'HasMFMA_bf16_original': False,
             'HasMFMA_constSrc': False,
             'HasMFMA_f64': False,
             'HasMFMA_f8': False,
             'HasMFMA_i8_908': False,
             'HasMFMA_i8_940': False,
             'HasMFMA_vgpr': False,
             'HasMFMA_xf32': False,
             'HasSMulHi': True,
             'HasWMMA': False,
             'KernargPreloading': False,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 63,
             'SupportedISA': True,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': True,
             'v_dot2_f32_f16': True,
             'v_dot2c_f32_f16': False,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': False,
             'v_fma_f16': True,
             'v_fma_f32': True,
             'v_fma_f64': True,
             'v_fma_mix_f32': True,
             'v_fmac_f16': False,
             'v_fmac_f32': True,
             'v_mac_f16': True,
             'v_mac_f32': True,
             'v_mad_mix_f32': False,
             'v_mov_b64': False,
             'v_pk_fma_f16': True,
             'v_pk_fmac_f16': False},
 (9, 0, 8): {'HasAddLshl': True,
             'HasAtomicAdd': True,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': True,
             'HasExplicitCO': True,
             'HasExplicitNC': False,
             'HasGLCModifier': True,
             'HasNTModifier': False,
             'HasLshlOr': True,
             'HasMFMA': True,
             'HasMFMA_b8': False,
             'HasMFMA_bf16_1k': False,
             'HasMFMA_bf16_original': True,
             'HasMFMA_constSrc': False,
             'HasMFMA_f64': False,
             'HasMFMA_f8': False,
             'HasMFMA_i8_908': True,
             'HasMFMA_i8_940': False,
             'HasMFMA_vgpr': False,
             'HasMFMA_xf32': False,
             'HasSMulHi': True,
             'HasWMMA': False,
             'KernargPreloading': False,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 63,
             'SupportedISA': True,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': True,
             'v_dot2_f32_f16': True,
             'v_dot2c_f32_f16': True,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': True,
             'v_fma_f16': True,
             'v_fma_f32': True,
             'v_fma_f64': True,
             'v_fma_mix_f32': True,
             'v_fmac_f16': False,
             'v_fmac_f32': True,
             'v_mac_f16': True,
             'v_mac_f32': True,
             'v_mad_mix_f32': False,
             'v_mov_b64': False,
             'v_pk_fma_f16': True,
             'v_pk_fmac_f16': False},
 (9, 0, 10): {'HasAddLshl': True,
              'HasAtomicAdd': True,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': True,
              'HasExplicitCO': True,
              'HasExplicitNC': False,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': True,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': True,
              'HasMFMA_bf16_original': True,
              'HasMFMA_constSrc': True,
              'HasMFMA_f64': True,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': True,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': True,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': True,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': True,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': True,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': True,
              'v_mac_f32': True,
              'v_mad_mix_f32': False,
             'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (9, 4, 0): {'HasAddLshl': True,
             'HasAtomicAdd': True,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': True,
             'HasExplicitCO': True,
             'HasExplicitNC': False,
             'HasGLCModifier': False,
             'HasNTModifier': True,
             'HasLshlOr': True,
             'HasMFMA': True,
             'HasMFMA_b8': True,
             'HasMFMA_bf16_1k': True,
             'HasMFMA_bf16_original': False,
             'HasMFMA_constSrc': True,
             'HasMFMA_f64': True,
             'HasMFMA_f8': True,
             'HasMFMA_i8_908': False,
             'HasMFMA_i8_940': True,
             'HasMFMA_vgpr': True,
             'HasMFMA_xf32': True,
             'HasSMulHi': True,
             'HasWMMA': False,
             'KernargPreloading': True,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 63,
             'SupportedISA': True,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': True,
             'v_dot2_f32_f16': True,
             'v_dot2c_f32_f16': True,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': True,
             'v_fma_f16': True,
             'v_fma_f32': True,
             'v_fma_f64': True,
             'v_fma_mix_f32': True,
             'v_fmac_f16': False,
             'v_fmac_f32': True,
             'v_mac_f16': True,
             'v_mac_f32': False,
             'v_mad_mix_f32': False,
             'v_mov_b64': True,
             'v_pk_fma_f16': True,
             'v_pk_fmac_f16': False},
 (9, 4, 1): {'HasAddLshl': True,
             'HasAtomicAdd': True,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': True,
             'HasExplicitCO': True,
             'HasExplicitNC': False,
             'HasGLCModifier': False,
             'HasNTModifier': True,
             'HasLshlOr': True,
             'HasMFMA': True,
             'HasMFMA_b8': True,
             'HasMFMA_bf16_1k': True,
             'HasMFMA_bf16_original': False,
             'HasMFMA_constSrc': True,
             'HasMFMA_f64': True,
             'HasMFMA_f8': True,
             'HasMFMA_i8_908': False,
             'HasMFMA_i8_940': True,
             'HasMFMA_vgpr': True,
             'HasMFMA_xf32': True,
             'HasSMulHi': True,
             'HasWMMA': False,
             'KernargPreloading': True,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 63,
             'SupportedISA': True,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': True,
             'v_dot2_f32_f16': True,
             'v_dot2c_f32_f16': True,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': True,
             'v_fma_f16': True,
             'v_fma_f32': True,
             'v_fma_f64': True,
             'v_fma_mix_f32': True,
             'v_fmac_f16': False,
             'v_fmac_f32': True,
             'v_mac_f16': True,
             'v_mac_f32': False,
             'v_mad_mix_f32': False,
             'v_mov_b64': True,
             'v_pk_fma_f16': True,
             'v_pk_fmac_f16': False},
 (9, 4, 2): {'HasAddLshl': True,
             'HasAtomicAdd': True,
             'HasDirectToLdsDest': False,
             'HasDirectToLdsNoDest': True,
             'HasExplicitCO': True,
             'HasExplicitNC': False,
             'HasGLCModifier': False,
             'HasNTModifier': True,
             'HasLshlOr': True,
             'HasMFMA': True,
             'HasMFMA_b8': True,
             'HasMFMA_bf16_1k': True,
             'HasMFMA_bf16_original': False,
             'HasMFMA_constSrc': True,
             'HasMFMA_f64': True,
             'HasMFMA_f8': True,
             'HasMFMA_i8_908': False,
             'HasMFMA_i8_940': True,
             'HasMFMA_vgpr': True,
             'HasMFMA_xf32': True,
             'HasSMulHi': True,
             'HasWMMA': False,
             'KernargPreloading': True,
             'MaxLgkmcnt': 15,
             'MaxVmcnt': 63,
             'SupportedISA': True,
             'SupportedSource': True,
             'VOP3v_dot4_i32_i8': True,
             'v_dot2_f32_f16': True,
             'v_dot2c_f32_f16': True,
             'v_dot4_i32_i8': False,
             'v_dot4c_i32_i8': True,
             'v_fma_f16': True,
             'v_fma_f32': True,
             'v_fma_f64': True,
             'v_fma_mix_f32': True,
             'v_fmac_f16': False,
             'v_fmac_f32': True,
             'v_mac_f16': True,
             'v_mac_f32': False,
             'v_mad_mix_f32': False,
             'v_mov_b64': True,
             'v_pk_fma_f16': True,
             'v_pk_fmac_f16': False},
 (10, 1, 0): {'HasAddLshl': True,
              'HasAtomicAdd': False,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': True,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': False,
              'v_dot2_f32_f16': False,
              'v_dot2c_f32_f16': False,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': False,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': True,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (10, 1, 1): {'HasAddLshl': True,
              'HasAtomicAdd': False,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': True,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': True,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': True,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': True,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (10, 1, 2): {'HasAddLshl': True,
              'HasAtomicAdd': False,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': True,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': True,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': True,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': True,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (10, 3, 0): {'HasAddLshl': True,
              'HasAtomicAdd': False,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': True,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': True,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': True,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (10, 3, 1): {'HasAddLshl': True,
              'HasAtomicAdd': False,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': True,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': True,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': True,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (11, 0, 0): {'HasAddLshl': True,
              'HasAtomicAdd': True,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': False,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': True,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': False,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': False,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (11, 0, 1): {'HasAddLshl': True,
              'HasAtomicAdd': True,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': False,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': True,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': False,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': False,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (11, 0, 2): {'HasAddLshl': True,
              'HasAtomicAdd': True,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': False,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': True,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': False,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': False,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (11, 5, 1): {'HasAddLshl': True,
              'HasAtomicAdd': True,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': False,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': True,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': True,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': False,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': True,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': False,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (12, 0, 0): {'HasAddLshl': True,
              'HasAtomicAdd': False,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': False,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': False,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': False,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': False,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': False,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False},
 (12, 0, 1): {'HasAddLshl': True,
              'HasAtomicAdd': False,
              'HasDirectToLdsDest': False,
              'HasDirectToLdsNoDest': False,
              'HasExplicitCO': True,
              'HasExplicitNC': True,
              'HasGLCModifier': False,
              'HasNTModifier': False,
              'HasLshlOr': True,
              'HasMFMA': False,
              'HasMFMA_b8': False,
              'HasMFMA_bf16_1k': False,
              'HasMFMA_bf16_original': False,
              'HasMFMA_constSrc': False,
              'HasMFMA_f64': False,
              'HasMFMA_f8': False,
              'HasMFMA_i8_908': False,
              'HasMFMA_i8_940': False,
              'HasMFMA_vgpr': False,
              'HasMFMA_xf32': False,
              'HasSMulHi': True,
              'HasWMMA': False,
              'KernargPreloading': False,
              'MaxLgkmcnt': 15,
              'MaxVmcnt': 63,
              'SupportedISA': True,
              'SupportedSource': True,
              'VOP3v_dot4_i32_i8': False,
              'v_dot2_f32_f16': True,
              'v_dot2c_f32_f16': False,
              'v_dot4_i32_i8': False,
              'v_dot4c_i32_i8': False,
              'v_fma_f16': True,
              'v_fma_f32': True,
              'v_fma_f64': True,
              'v_fma_mix_f32': True,
              'v_fmac_f16': False,
              'v_fmac_f32': True,
              'v_mac_f16': False,
              'v_mac_f32': False,
              'v_mad_mix_f32': False,
              'v_mov_b64': False,
              'v_pk_fma_f16': True,
              'v_pk_fmac_f16': False}}
